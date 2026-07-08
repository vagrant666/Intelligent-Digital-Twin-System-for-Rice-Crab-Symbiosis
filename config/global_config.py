"""
全局基础配置
农场基准参数、路径、训练超参、算法统一管理
全部数据依赖官方联网API，无仿真开关
"""
import os

# 项目根路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_RAW = os.path.join(BASE_DIR, "data", "raw")
DATA_PROCESSED = os.path.join(BASE_DIR, "data", "processed")
DATASET_DIR = os.path.join(BASE_DIR, "data", "dataset")
CKPT_DIR = os.path.join(BASE_DIR, "data", "checkpoint")
LOG_DIR = os.path.join(BASE_DIR, "logs")
OUTPUT_EXCEL = os.path.join(BASE_DIR, "output", "excel_report")
OUTPUT_FIG = os.path.join(BASE_DIR, "output", "figures")

# 自动创建全部工作目录
for path in [DATA_RAW, DATA_PROCESSED, DATASET_DIR, CKPT_DIR, LOG_DIR, OUTPUT_EXCEL, OUTPUT_FIG]:
    os.makedirs(path, exist_ok=True)

# 标准温带80亩稻蟹农场基准参数
FARM_AREA_ACRE = 80
GROWTH_CYCLE_DAYS = 125
CRAB_STOCKING_DENSITY_RANGE = [220, 680]
RICE_YIELD_RANGE = [420, 580]
CRAB_YIELD_RANGE = [12, 38]

# API采集地理范围
LAT = 39.31
LON = 117.33
DATA_START_YEAR = 2015
DATA_END_YEAR = 2025

# API请求限流配置
API_INTERVAL = 2.0
API_MAX_RETRY = 3

# 深度学习训练核心参数
TOTAL_EPOCHS = 1000
BATCH_SIZE = 32
LEARNING_RATE = 1e-3
LR_DECAY_GAMMA = 0.98
EARLY_STOP_PATIENCE = 30
TRAIN_VAL_TEST_RATIO = [0.7, 0.15, 0.15]

# 模型通用超参
LSTM_HIDDEN = 128
LSTM_LAYER = 3
ATTENTION_DIM = 64
CNN_FILTER = 64
TRANSFORMER_HEAD = 8
DROPOUT_RATE = 0.25

# NSGA-II多目标优化
NSGA_POP = 200
NSGA_GEN = 300

# GA无人机路径规划
UAV_POP = 150
UAV_GEN = 200
