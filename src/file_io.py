import os
import json
import pandas as pd
import numpy as np

def save_json(data, save_path):
    with open(save_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def load_json(load_path):
    with open(load_path, "r", encoding="utf-8") as f:
        return json.load(f)

def check_file_exist(file_path):
    return os.path.exists(file_path)

def clear_dir(dir_path):
    if os.path.exists(dir_path):
        for file in os.listdir(dir_path):
            os.remove(os.path.join(dir_path, file))
