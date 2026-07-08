"""
数据集清洗流水线：去重、时间格式化、缺失填充、3σ异常剔除
"""
import pandas as pd
import numpy as np
from config.data_config import MISS_FILL

class DataCleaner:
    def drop_duplicate(self, df):
        return df.drop_duplicates().reset_index(drop=True)

    def fill_missing_value(self, df):
        num_cols = df.select_dtypes(include=[np.number]).columns
        if MISS_FILL == "mean":
            df[num_cols] = df[num_cols].fillna(df[num_cols].mean())
        elif MISS_FILL == "median":
            df[num_cols] = df[num_cols].fillna(df[num_cols].median())
        elif MISS_FILL == "linear":
            df[num_cols] = df[num_cols].interpolate(method="linear")
        return df

    def remove_outlier_data(self, df, std_thresh=3):
        num_cols = df.select_dtypes(include=[np.number]).columns
        for col in num_cols:
            mu = df[col].mean()
            sigma = df[col].std()
            df = df[(df[col] >= mu - std_thresh * sigma) & (df[col] <= mu + std_thresh * sigma)]
        return df

    def format_datetime(self, df):
        df["date"] = pd.to_datetime(df["date"], errors="coerce")
        df = df.dropna(subset=["date"])
        df["date"] = df["date"].astype(str)
        return df

    def full_clean_pipeline(self, df):
        df = self.drop_duplicate(df)
        df = self.format_datetime(df)
        df = self.fill_missing_value(df)
        df = self.remove_outlier_data(df)
        return df.reset_index(drop=True)
