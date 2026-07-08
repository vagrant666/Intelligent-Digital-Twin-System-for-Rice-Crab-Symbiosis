import torch
import torch.nn as nn
from config.model_config import RESNET_CFG

class ResBlock(nn.Module):
    def __init__(self, dim, drop):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(dim, dim), nn.ReLU(), nn.Dropout(drop),
            nn.Linear(dim, dim), nn.Dropout(drop)
        )
        self.relu = nn.ReLU()
    def forward(self, x):
        return self.relu(x + self.net(x))

class ResNetYieldModel(nn.Module):
    def __init__(self):
        super().__init__()
        cfg = RESNET_CFG
        self.in_proj = nn.Linear(cfg["in_features"] * 12, cfg["hidden_width"])
        self.blocks = nn.Sequential(*[ResBlock(cfg["hidden_width"], cfg["dropout"]) for _ in range(cfg["res_block_num"])])
        self.out_proj = nn.Linear(cfg["hidden_width"], 2)
    def forward(self, x):
        x = x.flatten(1)
        x = self.in_proj(x)
        x = self.blocks(x)
        return self.out_proj(x)
