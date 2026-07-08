import matplotlib.pyplot as plt
import numpy as np
import os
from config.global_config import OUTPUT_FIG
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

def plot_uav_route(route_points, total_dist):
    plt.figure(figsize=(10,6))
    plt.scatter(route_points[:,0], route_points[:,1], c="red", s=40, label="巡检点位")
    plt.plot(route_points[:,0], route_points[:,1], color="#1F77B4", linewidth=1.5, alpha=0.8)
    plt.scatter(route_points[0,0], route_points[0,1], c="green", s=100, label="起点")
    plt.scatter(route_points[-1,0], route_points[-1,1], c="orange", s=100, label="终点")
    plt.title(f"农田无人机最优巡检路径（总距离：{total_dist:.2f}m）")
    plt.xlabel("农田X坐标")
    plt.ylabel("农田Y坐标")
    plt.legend()
    plt.grid(alpha=0.3)
    save_path = os.path.join(OUTPUT_FIG, "uav_best_route.png")
    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches="tight")
    plt.close()
    return save_path
