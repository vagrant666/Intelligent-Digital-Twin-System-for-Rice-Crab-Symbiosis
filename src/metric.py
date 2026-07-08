import numpy as np

def calc_rmse(pred, label):
    return np.sqrt(np.mean(np.square(pred)))

def calc_mae(pred, label):
    return np.mean(np.abs(pred))

def calc_r2(pred, label):
    ss_res = np.sum((label - pred) ** 2)
    ss_tot = np.sum((label - np.mean(label)) ** 2)
    return 1 - ss_res / (ss_tot + 1e-8)
