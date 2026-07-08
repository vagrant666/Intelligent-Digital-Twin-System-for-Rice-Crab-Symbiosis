import logging
import os
from config.global_config import LOG_DIR

def init_logger():
    os.makedirs(LOG_DIR, exist_ok=True)
    log_path = os.path.join(LOG_DIR, "system_run.log")
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s \| %(levelname)s \| %(message)s",
        handlers=[
            logging.FileHandler(log_path, encoding="utf-8"),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger()

logger = init_logger()
