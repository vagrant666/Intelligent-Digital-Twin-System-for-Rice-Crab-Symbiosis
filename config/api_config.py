"""
NASA / FAO 官方API接口配置
纯联网模式，无离线仿真开关
"""
NASA_API_ROOT = "https://power.larc.nasa.gov/api/temporal/daily/point"
FAO_API_ROOT = "https://faostatservices.fao.org/api/v1/en/data/Production"

# 学术非商用合规请求头
COMMON_HEADERS = {
    "User-Agent": "Rice-Crab-Digital-Twin-OpenSource/1.0 (Academic Non-Commercial Research)",
    "Accept": "application/json",
    "Referer": "https://power.larc.nasa.gov/"
}

CACHE_TTL = 86400
API_TIMEOUT = 30
OFFLINE_RUN = False
