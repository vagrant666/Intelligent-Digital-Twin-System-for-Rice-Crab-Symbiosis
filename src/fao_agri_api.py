"""
FAOSTAT 全球农业统计数据采集
"""
from src.data_crawler.base_crawler import BaseCrawler
import pandas as pd
import os
import logging
from config.global_config import DATA_RAW, DATA_START_YEAR, DATA_END_YEAR
from config.api_config import FAO_API_ROOT

class FaoAgriCrawler:
    def fetch_rice_crab_stat(self):
        crawler = BaseCrawler()
        params = {
            "element": "Production,Value,InputCost",
            "item": "Rice, Freshwater crustaceans, Fertilizers, Feed",
            "area": "Asia",
            "year": ",".join([str(y) for y in range(DATA_START_YEAR, DATA_END_YEAR+1)])
        }
        raw_json = crawler.safe_request(FAO_API_ROOT, params)
        df = pd.DataFrame(raw_json["data"])
        save_path = os.path.join(DATA_RAW, "fao_rice_crab_10y.csv")
        df.to_csv(save_path, index=False, encoding="utf-8-sig")
        logging.info("FAO农业统计数据采集完成")
        return df
