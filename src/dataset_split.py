"""
构建时序样本并严格按时间划分训练/验证/测试集，不打乱顺序
"""
import numpy as np
import os
from config.global_config import DATASET_DIR
from config.data_config import TRAIN_RATIO, VAL_RATIO, SEQ_WINDOW, PRED_LEN, FEATURE_COLS, TARGET_COL

class TimeSeriesDatasetSplitter:
    def build_sequence_dataset(self, df_scaled):
        feat = df_scaled[FEATURE_COLS].values
        label = df_scaled[TARGET_COL].values
        x_seq, y_seq = [], []
        for i in range(SEQ_WINDOW, len(feat) - PRED_LEN + 1):
            x_seq.append(feat[i-SEQ_WINDOW:i, :])
            y_seq.append(label[i:i+PRED_LEN, :])
        x_all = np.array(x_seq, dtype=np.float32)
        y_all = np.array(y_seq, dtype=np.float32)
        total = len(x_all)
        train_end = int(total * TRAIN_RATIO)
        val_end = train_end + int(total * VAL_RATIO)
        x_train, y_train = x_all[:train_end], y_all[:train_end]
        x_val, y_val = x_all[train_end:val_end], y_all[train_end:val_end]
        x_test, y_test = x_all[val_end:], y_all[val_end:]
        np.save(os.path.join(DATASET_DIR, "x_train.npy"), x_train)
        np.save(os.path.join(DATASET_DIR, "y_train.npy"), y_train)
        np.save(os.path.join(DATASET_DIR, "x_val.npy"), x_val)
        np.save(os.path.join(DATASET_DIR, "y_val.npy"), y_val)
        np.save(os.path.join(DATASET_DIR, "x_test.npy"), x_test)
        np.save(os.path.join(DATASET_DIR, "y_test.npy"), y_test)
        print(f"数据集构建完成：train{x_train.shape}, val{x_val.shape}, test{x_test.shape}")
        return (x_train, y_train), (x_val, y_val), (x_test, y_test)
