import pandas as pd
import os
from config.global_config import OUTPUT_EXCEL

def export_full_report(data_stat, model_metric, pareto_res, risk_res, uav_dist):
    os.makedirs(OUTPUT_EXCEL, exist_ok=True)
    save_path = os.path.join(OUTPUT_EXCEL, "稻蟹数字孪生系统分析报告.xlsx")
    with pd.ExcelWriter(save_path, engine="openpyxl") as writer:
        pd.DataFrame([data]).to_excel(writer, sheet_name="数据集统计", index=False)
        pd.DataFrame([model_metric]).to_excel(writer, sheet_name="模型性能指标", index=False)
        pd.DataFrame(pareto_res).to_excel(writer, sheet_name="种养优化解集", index=False)
        pd.DataFrame([risk_res]).to_excel(writer, sheet_name="风险评估结果", index=False)
        pd.DataFrame([{"最优巡检总距离": round(uav_dist,2)}]).to_excel(writer, sheet_name="巡检路径参数", index=False)
    return save_path
