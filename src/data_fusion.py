"""
多源数据表时序合并融合
"""
import pandas as pd
import os
from config.global_config import DATA_PROCESSED

class DataFusionCleaner:
    def merge_all_source_data(self, nasa_df, soil_df, pest_df, ndvi_df):
        df = pd.merge(nasa_df, soil_df, on="date", how="left")
        df = pd.merge(df, pest_df, on="date", how="left")
        df = pd.merge(df, ndvi_df, on="date", how="left")
        df = df.fillna(method="ffill").fillna(method="bfill")
        save_path = os.path.join(DATA_PROCESSED, "fusion_all_feature_data.csv")
        df.to_csv(save_path, index=False, encoding="utf-8-sig")
        return df
