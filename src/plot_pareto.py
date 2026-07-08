import matplotlib.pyplot as plt
import numpy as np
import os
from config.global_config import OUTPUT_FIG
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

def plot_pareto_front(pareto_data):
    rice_y = -pareto_data[:,0]
    crab_y = -pareto_data[:,1]
    cost = pareto_data[:,2]
    fig, ax = plt.subplots(figsize=(10,7))
    scatter = ax.scatter(rice_y, crab_y, c=cost, s=30, alpha=0.7, cmap="viridis")
    plt.colorbar(scatter, label="种养成本")
    ax.set_xlabel("水稻产量")
    ax.set_ylabel("河蟹产量")
    ax.set_title("稻蟹种养多目标优化帕累托前沿解集")
    ax.grid(alpha=0.3)
    save_path = os.path.join(OUTPUT_FIG, "pareto_front.png")
    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches="tight")
    plt.close()
    return save_path
