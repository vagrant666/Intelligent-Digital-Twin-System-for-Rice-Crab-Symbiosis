from torch.optim.lr_scheduler import ExponentialLR
from config.global_config import LR_DECAY_GAMMA

class WarmupDecayLR(ExponentialLR):
    def __init__(self, optimizer):
        super().__init__(optimizer, gamma=LR_DECAY_GAMMA)
