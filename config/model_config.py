"""
各深度学习模型独立超参配置
"""
from config.global_config import LSTM_HIDDEN, LSTM_LAYER, ATTENTION_DIM, CNN_FILTER, TRANSFORMER_HEAD, DROPOUT_RATE

# LSTM-Attention
LSTM_ATTENTION_CFG = {
    "input_dim": 12,
    "hidden_dim": LSTM_HIDDEN,
    "layer_num": LSTM_LAYER,
    "attn_dim": ATTENTION_DIM,
    "dropout": DROPOUT_RATE
}

# CNN-Transformer
CNN_TRANS_CFG = {
    "input_dim": 12,
    "embed_dim": CNN_FILTER,
    "n_head": TRANSFORMER_HEAD,
    "layer_num": 3,
    "dropout": DROPOUT_RATE
}

# 残差回归网络
RESNET_CFG = {
    "in_features": 12,
    "hidden_width": 128,
    "res_block_num": 4,
    "dropout": DROPOUT_RATE
}

# SSA-BP参数
SSA_BP_CFG = {
    "bp_hidden": 64,
    "ssa_pop": 30,
    "ssa_iter": 80,
    "lb": -1,
    "ub": 1
}
