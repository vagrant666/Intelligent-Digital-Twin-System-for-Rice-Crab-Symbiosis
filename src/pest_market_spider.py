"""
病虫害风险、农产品市场价格采集
"""
from src.data_crawler.base_crawler import BaseCrawler
import pandas as pd
import os
import logging
from config.global_config import DATA_RAW

class PestMarketSpider:
    def fetch_pest_market_data(self):
        crawler = BaseCrawler()
        url = "https://opendata.agri-public.org/api/market_pest"
        params = {"product":["rice","freshwater_crab"],"time_range":"10y"}
        raw = crawler.safe_request(url, params)
        df = pd.DataFrame(raw["data"])
        save_path = os.path.join(DATA_RAW, "pest_market_raw.csv")
        df.to_csv(save_path, index=False, encoding="utf-8-sig")
        logging.info("病虫害与市场价格数据采集完成")
        return df
