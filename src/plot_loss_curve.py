import matplotlib.pyplot as plt
import os
from config.global_config import OUTPUT_FIG
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

def plot_loss_curve(train_loss, val_loss):
    plt.figure(figsize=(10,6))
    plt.plot(train_loss, label="训练损失", color="#2E86AB", linewidth=2)
    plt.plot(val_loss, label="验证损失", color="#A23B72", linewidth=2)
    plt.xlabel("训练轮次 Epoch")
    plt.ylabel("损失值 Loss")
    plt.title("模型训练损失变化曲线")
    plt.legend()
    plt.grid(alpha=0.3)
    save_path = os.path.join(OUTPUT_FIG, "loss_curve.png")
    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches="tight")
    plt.close()
    return save_path
