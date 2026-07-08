"""
数据集处理专用配置：时序窗口、归一化、特征列表、缺失填充
"""
from config.global_config import TRAIN_VAL_TEST_RATIO

SEQ_WINDOW = 12
PRED_LEN = 7
SCALE_TYPE = "minmax"
SCALE_MIN = 0
SCALE_MAX = 1
TRAIN_RATIO, VAL_RATIO, TEST_RATIO = TRAIN_VAL_TEST_RATIO
AUG_NOISE_SCALE = 0.015
MISS_FILL = "linear"

# 输入特征列
FEATURE_COLS = [
    "temp", "humidity", "wind_speed", "radiation",
    "rainfall", "evap", "nitrogen", "phosphorus",
    "potassium", "ph", "ndvi", "crab_density"
]
# 预测双目标：水稻产量、河蟹产量
TARGET_COL = ["rice_yield", "crab_yield"]
