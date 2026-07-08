import torch
import os
from config.global_config import CKPT_DIR

class EarlyStopping:
    def __init__(self, patience=30, save_name="best_model.pth"):
        self.patience = patience
        self.save_path = os.path.join(CKPT_DIR, save_name)
        self.counter = 0
        self.best_loss = float("inf")
        self.early_stop = False

    def __call__(self, val_loss, model):
        if val_loss < self.best_loss:
            self.best_loss = val_loss
            self.counter = 0
            torch.save(model.state_dict(), self.save_path)
        else:
            self.counter += 1
            if self.counter >= self.patience:
                self.early_stop = True
