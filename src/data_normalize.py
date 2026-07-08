"""
数据归一化，保存缩放器用于推理逆转换
"""
import pandas as pd
import numpy as np
import joblib
import os
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from config.global_config import DATA_PROCESSED
from config.data_config import SCALE_TYPE, SCALE_MIN, SCALE_MAX

class DataNormalizer:
    def __init__(self):
        self.scaler = None
        self.save_path = os.path.join(DATA_PROCESSED, "feature_scaler.pkl")

    def fit_transform_data(self, df):
        num_df = df.select_dtypes(include=[np.number])
        if SCALE_TYPE == "minmax":
            self.scaler = MinMaxScaler((SCALE_MIN, SCALE_MAX))
        else:
            self.scaler = StandardScaler()
        scaled_arr = self.scaler.fit_transform(num_df)
        scaled_df = pd.DataFrame(scaled_arr, columns=num_df.columns)
        joblib.dump(self.scaler, self.save_path)
        return scaled_df

    def inverse_scale(self, arr):
        return self.scaler.inverse_transform(arr)
