"""
模型基类：统一权重保存、加载、断点续训
"""
import torch
import os
from config.global_config import CKPT_DIR

class BaseDLModel(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def save_checkpoint(self, name="last_epoch_model.pth"):
        path = os.path.join(CKPT_DIR, name)
        torch.save({"model_state_dict": self.state_dict()}, path)
        return path

    def load_checkpoint(self, name="best_model.pth"):
        path = os.path.join(CKPT_DIR, name)
        ckpt = torch.load(path, map_location="cpu")
        self.load_state_dict(ckpt["model_state_dict"])
        self.eval()
        return self
