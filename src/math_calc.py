import numpy as np

def min_max_scale(x, x_min, x_max):
    return (x - x_min) / (x_max - x_min + 1e-8)

def inverse_min_max_scale(x, x_min, x_max):
    return x * (x_max - x_min) + x_min

def calc_mean_std(arr):
    return np.mean(arr), np.std(arr)

def round_list(data_list, decimals=2):
    return [round(x, decimals) for x in data_list]
