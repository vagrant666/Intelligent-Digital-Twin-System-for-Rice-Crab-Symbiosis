import matplotlib.pyplot as plt
import os
from config.global_config import OUTPUT_FIG
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

def plot_metric_curve(r2_list, mae_list):
    fig, (ax1, ax2) = plt.subplots(1,2,figsize=(14,6))
    ax1.plot(r2_list, color="#27AE60", linewidth=2, label="R² Score")
    ax1.set_xlabel("训练轮次 Epoch")
    ax1.set_ylabel("R² 决定系数")
    ax1.set_title("模型R²精度变化曲线")
    ax1.grid(alpha=0.3)
    ax1.legend()
    ax2.plot(mae_list, color="#E74C3C", linewidth=2, label="MAE")
    ax2.set_xlabel("训练轮次 Epoch")
    ax2.set_ylabel("平均绝对误差 MAE")
    ax2.set_title("模型MAE误差变化曲线")
    ax2.grid(alpha=0.3)
    ax2.legend()
    save_path = os.path.join(OUTPUT_FIG, "metric_curve.png")
    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches="tight")
    plt.close()
    return save_path
