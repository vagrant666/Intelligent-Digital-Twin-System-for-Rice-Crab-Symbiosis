"""
单元测试脚本
"""
import sys
sys.path.append("./")
from config.global_config import *
from src.utils.math_calc import min_max_scale, inverse_min_max_scale
from src.train.metric import calc_r2, calc_mae
import numpy as np

def test_math_util():
    x = np.array([1,2,3,4,5])
    scaled = min_max_scale(x, x.min(), x.max())
    inv = inverse_min_max_scale(scaled, x.min(), x.max())
    assert np.allclose(x, inv)
    print("数学工具测试通过")

def test_metric():
    pred = np.array([0.1,0.2,0.3])
    label = np.array([0.11,0.22,0.29])
    r2 = calc_r2(pred, label)
    mae = calc_mae(pred, label)
    assert r2 > 0.9
    assert mae < 0.02
    print("评价指标测试通过")

if __name__ == "__main__":
    test_math_util()
    test_metric()
    print("全部单元测试执行完成")
