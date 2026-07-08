import numpy as np
import torch
import torch.nn as nn
from config.model_config import SSA_BP_CFG

class BPNeuralNetwork(nn.Module):
    def __init__(self, hid_dim):
        super().__init__()
        self.fc1 = nn.Linear(12, hid_dim)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hid_dim, 2)
    def forward(self, x):
        return self.fc2(self.relu(self.fc1(x)))

class SSABPModel:
    def __init__(self):
        self.cfg = SSA_BP_CFG
        self.model = BPNeuralNetwork(self.cfg["bp_hidden"])
        self.lb, self.ub = self.cfg["lb"], self.cfg["ub"]

    def get_param_flat_num(self):
        return sum(p.numel() for p in self.model.parameters())

    def update_params(self, flat_arr):
        idx = 0
        for p in self.model.parameters():
            n = p.numel()
            p.data = torch.tensor(flat_arr[idx:idx+n].reshape(p.shape), dtype=torch.float32)
            idx += n

    def fitness(self, flat_params, x, y):
        self.update_params(flat_params)
        pred = self.model(x)
        return torch.mean(torch.square(pred - y)).item()

    def optimize(self, x_data, y_data):
        pop = np.random.uniform(self.lb, self.ub, (self.cfg["ssa_pop"], self.get_param_flat_num()))
        best_loss = float("inf")
        best_params = None
        for it in range(self.cfg["ssa_iter"]):
            fits = [self.fitness(p, x_data, y_data) for p in pop]
            best_idx = np.argmin(fits)
            if fits[best_idx] < best_loss:
                best_loss = fits[best_idx]
                best_params = pop[best_idx].copy()
            disc_num = int(0.2 * len(pop))
            sort_idx = np.argsort(fits)
            discoverers = pop[sort_idx[:disc_num]]
            for i in range(len(discoverers)):
                r2 = np.random.rand()
                if r2 < 0.8:
                    discoverers[i] = discoverers[i] * np.exp(-i / (np.random.rand() * self.cfg["ssa_iter"]))
                else:
                    discoverers[i] += np.random.normal(0,1,discoverers[i].shape)
            pop[sort_idx[:disc_num]] = discoverers
        self.update_params(best_params)
        return self.model
