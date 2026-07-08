import torch
import torch.nn as nn
from config.model_config import LSTM_ATTENTION_CFG

class AttentionBlock(nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.attn = nn.Sequential(nn.Linear(dim, dim), nn.Tanh(), nn.Linear(dim,1,bias=False))
    def forward(self, x):
        w = torch.softmax(self.attn(x), dim=1)
        return torch.sum(x * w, dim=1)

class LstmAttentionModel(nn.Module):
    def __init__(self):
        super().__init__()
        cfg = LSTM_ATTENTION_CFG
        self.lstm = nn.LSTM(cfg["input_dim"], cfg["hidden_dim"], cfg["layer_num"], batch_first=True, dropout=cfg["dropout"])
        self.attn = AttentionBlock(cfg["hidden_dim"])
        self.fc = nn.Linear(cfg["hidden_dim"], 2)
    def forward(self, x):
        out, _ = self.lstm(x)
        att_out = self.attn(out)
        return self.fc(att_out)
