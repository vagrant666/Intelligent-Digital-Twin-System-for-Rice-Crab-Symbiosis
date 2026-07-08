import torch
import torch.nn as nn
from config.model_config import CNN_TRANS_CFG

class CNNTransformerAgriculture(nn.Module):
    def __init__(self):
        super().__init__()
        cfg = CNN_TRANS_CFG
        self.cnn_backbone = nn.Sequential(
            nn.Conv1d(cfg["input_dim"], 64, 3, padding=1),
            nn.BatchNorm1d(64),
            nn.ReLU(),
            nn.Dropout(cfg["dropout"]),
            nn.Conv1d(64, cfg["embed_dim"], 3, padding=1),
            nn.BatchNorm1d(cfg["embed_dim"]),
            nn.ReLU()
        )
        encoder_layer = nn.TransformerEncoderLayer(d_model=cfg["embed_dim"], nhead=cfg["n_head"], dropout=cfg["dropout"], batch_first=True)
        self.transformer_encoder = nn.TransformerEncoder(encoder_layer, num_layers=cfg["layer_num"])
        self.fc_out = nn.Sequential(
            nn.Linear(cfg["embed_dim"], 32),
            nn.ReLU(),
            nn.Linear(32, 2)
        )

    def forward(self, x):
        x = x.transpose(1,2)
        cnn_feat = self.cnn_backbone(x)
        cnn_feat = cnn_feat.transpose(1,2)
        trans_feat = self.transformer_encoder(cnn_feat)
        return self.fc_out(trans_feat[:, -1, :])
