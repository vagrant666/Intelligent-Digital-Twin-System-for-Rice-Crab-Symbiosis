"""
公开农业土壤养分API采集
"""
from src.data_crawler.base_crawler import BaseCrawler
import pandas as pd
import os
import logging
from config.global_config import DATA_RAW

class SoilNutrientSpider:
    def fetch_soil_benchmark(self):
        crawler = BaseCrawler()
        url = "https://opendata.agri-public.org/api/soil/nutrient"
        params = {"region_type":"temperate_plain","crop_type":"rice_crab"}
        raw = crawler.safe_request(url, params)
        df = pd.DataFrame(raw["dataset"])
        save_path = os.path.join(DATA_RAW, "soil_nutrient_raw.csv")
        df.to_csv(save_path, index=False, encoding="utf-8-sig")
        logging.info(f"土壤养分数据采集完成，样本量：{len(df)}")
        return df
