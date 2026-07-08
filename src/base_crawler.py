"""
API请求基类：统一缓存、重试、限流、异常捕获
仅支持联网真实API，禁止仿真数据生成
"""
import time
import requests
from cachetools import TTLCache
import logging
from config.global_config import API_INTERVAL, API_MAX_RETRY
from config.api_config import COMMON_HEADERS, CACHE_TTL, API_TIMEOUT, OFFLINE_RUN

global_cache = TTLCache(maxsize=500, ttl=CACHE_TTL)
logging.basicConfig(level=logging.INFO, format="[CRAWLER] %(asctime)s \| %(message)s")

class BaseCrawler:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update(COMMON_HEADERS)
        self.request_interval = API_INTERVAL
        self.max_retry = API_MAX_RETRY
        self.offline_mode = OFFLINE_RUN

    def safe_request(self, url, params=None):
        if self.offline_mode:
            raise ConnectionError("本项目仅支持联网官方真实API，不提供离线仿真数据")
        cache_key = f"{url}_{str(params)}"
        if cache_key in global_cache:
            logging.info(f"接口缓存命中：{cache_key}")
            return global_cache[cache_key]
        retry_cnt = 0
        while retry_cnt < self.max_retry:
            try:
                resp = self.session.get(url, params=params, timeout=API_TIMEOUT)
                resp.raise_for_status()
                res_json = resp.json(strict=False)
                global_cache[cache_key] = res_json
                time.sleep(self.request_interval)
                logging.info(f"API请求成功：{url}")
                return res_json
            except Exception as e:
                retry_cnt += 1
                wait = self.request_interval * retry_cnt
                logging.warning(f"请求失败，重试{retry_cnt}/{self.max_retry}，等待{wait}s，错误：{str(e)}")
                time.sleep(wait)
        raise ConnectionError(f"连续{self.max_retry}次API请求失败，请检查网络或官方接口可用性")
