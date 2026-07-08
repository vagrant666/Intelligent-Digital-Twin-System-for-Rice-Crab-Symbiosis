"""
时序数据高斯噪声增强，缓解过拟合
"""
import numpy as np
from config.data_config import AUG_NOISE_SCALE

class DataAugmentor:
    def gaussian_noise_augment(self, data):
        noise = np.random.normal(0, AUG_NOISE_SCALE, size=data.shape)
        aug = data + noise
        return np.clip(aug, 0, 1)
