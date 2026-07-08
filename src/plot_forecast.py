import matplotlib.pyplot as plt
import numpy as np
import os
from config.global_config import OUTPUT_FIG
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

def plot_forecast_curve(history_data, pred_data, ci_data, name="产量"):
    plt.figure(figsize=(12,6))
    plt.plot(history_data, color="#2E86AB", linewidth=2, label=f"历史{name}")
    pred_x = np.arange(len(history_data), len(history_data)+len(pred_data))
    plt.plot(pred_x, pred_data, color="#E63946", linewidth=2, label=f"预测{name}")
    plt.fill_between(pred_x, ci_data[:,0], ci_data[:,1], color="#E63946", alpha=0.2, label="95%置信区间")
    plt.title(f"稻蟹{name}时序趋势预测曲线")
    plt.xlabel("时序天数")
    plt.ylabel(name)
    plt.legend()
    plt.grid(alpha=0.3)
    save_path = os.path.join(OUTPUT_FIG, f"{name}_forecast.png")
    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches="tight")
    plt.close()
    return save_path
