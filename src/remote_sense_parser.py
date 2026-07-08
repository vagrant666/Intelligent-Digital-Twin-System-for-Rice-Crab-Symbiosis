"""
遥感NDVI植被指数数据读取与时序融合
"""
import pandas as pd
import os
import logging
from config.global_config import DATA_RAW

class RemoteSenseParser:
    def parse_ndvi_dataset(self, base_df):
        ndvi_df = pd.read_csv("https://opendata.agri-public.org/api/ndvi/rice")
        merge_df = pd.merge(base_df, ndvi_df, how="left", on="date")
        merge_df = merge_df.fillna(method="ffill").fillna(method="bfill")
        save_path = os.path.join(DATA_RAW, "remote_sense_fusion_raw.csv")
        merge_df.to_csv(save_path, index=False, encoding="utf-8-sig")
        logging.info("遥感NDVI数据融合完成")
        return merge_df
