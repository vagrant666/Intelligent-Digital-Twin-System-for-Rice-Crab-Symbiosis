import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import TensorDataset, DataLoader
from tqdm import tqdm
import numpy as np
from config.global_config import *
from src.train.early_stopping import EarlyStopping
from src.train.lr_scheduler import WarmupDecayLR
from src.train.metric import calc_rmse, calc_mae, calc_r2

class DeepTrainer:
    def __init__(self, model, train_set, val_set, test_set):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model = model.to(self.device)
        self.train_loader = DataLoader(TensorDataset(*train_set), batch_size=BATCH_SIZE, shuffle=True, num_workers=0)
        self.val_loader = DataLoader(TensorDataset(*val_set), batch_size=BATCH_SIZE, shuffle=False)
        self.test_loader = DataLoader(TensorDataset(*test_set), batch_size=BATCH_SIZE, shuffle=False)
        self.criterion = nn.MSELoss()
        self.optimizer = optim.Adam(self.model.parameters(), lr=LEARNING_RATE, weight_decay=1e-4)
        self.scheduler = WarmupDecayLR(self.optimizer)
        self.early_stop = EarlyStopping(patience=EARLY_STOP_PATIENCE)
        self.train_loss_list = []
        self.val_loss_list = []
        self.r2_list = []
        self.mae_list = []

    def train_one_epoch(self):
        self.model.train()
        total_loss = 0.0
        for x, y in tqdm(self.train_loader, desc="Train Epoch"):
            x, y = x.to(self.device), y.to(self.device)
            self.optimizer.zero_grad()
            pred = self.model(x)
            loss = self.criterion(pred, y[:, -1, :])
            loss.backward()
            self.optimizer.step()
            total_loss += loss.item()
        return total_loss / len(self.train_loader)

    def val_one_epoch(self):
        self.model.eval()
        total_loss = 0.0
        all_pred, all_label = [], []
        with torch.no_grad():
            for x, y in self.val_loader:
                x, y = x.to(self.device), y.to(self.device)
                pred = self.model(x)
                loss = self.criterion(pred, y[:, -1, :])
                total_loss += loss.item()
                all_pred.append(pred.cpu().numpy())
                all_label.append(y[:, -1, :].cpu().numpy())
        all_pred = np.concatenate(all_pred)
        all_label = np.concatenate(all_label)
        r2 = calc_r2(all_pred, all_label)
        mae = calc_mae(all_pred, all_label)
        return total_loss / len(self.val_loader), r2, mae

    def full_train(self):
        print(f"\nStart full training total {TOTAL_EPOCHS} epochs, device: {self.device}")
        for epoch in range(1, TOTAL_EPOCHS+1):
            train_loss = self.train_one_epoch()
            val_loss, val_r2, val_mae = self.val_one_epoch()
            self.train_loss_list.append(train_loss)
            self.val_loss_list.append(val_loss)
            self.r2_list.append(val_r2)
            self.mae_list.append(val_mae)
            self.scheduler.step()
            print(f"Epoch {epoch:04d}/{TOTAL_EPOCHS} \| TrainLoss {train_loss:.6f} \| ValLoss {val_loss:.6f} \| R2 {val_r2:.4f} \| MAE {val_mae:.4f}")
            self.early_stop(val_loss, self.model)
            if self.early_stop.early_stop:
                print(f"Early stop triggered at epoch {epoch}")
                break
        print("Train finished")
        return self.train_loss_list, self.val_loss_list, self.r2_list, self.mae_list
