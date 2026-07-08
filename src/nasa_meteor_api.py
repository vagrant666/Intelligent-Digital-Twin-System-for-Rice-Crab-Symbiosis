"""
NASA POWER 10年逐日气象数据采集
"""
from src.data_crawler.base_crawler import BaseCrawler
import pandas as pd
import os
import logging
from config.global_config import *
from config.api_config import NASA_API_ROOT

class NasaMeteorCrawler:
    def fetch_10year_meteor(self):
        crawler = BaseCrawler()
        params = {
            "parameters":"T2M,RH2M,WS2M,ALLSKY_SFC_SW_DWN,PRECTOT,EVAPTRANS",
            "community":"AG",
            "latitude":LAT,
            "longitude":LON,
            "start":f"{DATA_START_YEAR}0101",
            "end":f"{DATA_END_YEAR}1231",
            "format":"JSON"
        }
        res = crawler.safe_request(NASA_API_ROOT, params)
        data = res["properties"]["parameter"]
        df_list = []
        for date in data["T2M"].keys():
            df_list.append({
                "date": date,
                "temp": data["T2M"][date],
                "humidity": data["RH2M"][date],
                "wind_speed": data["WS2M"][date],
                "radiation": data["ALLSKY_SFC_SW_DWN"][date],
                "rainfall": data["PRECTOT"][date],
                "evap": data["EVAPTRANS"][date]
            })
        df = pd.DataFrame(df_list)
        save_path = os.path.join(DATA_RAW, "nasa_10year_meteor.csv")
        df.to_csv(save_path, index=False, encoding="utf-8-sig")
        logging.info(f"NASA气象数据下载完成，样本量：{len(df)}")
        return df
