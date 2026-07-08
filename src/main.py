from src.data_crawler.nasa_meteor_api import NasaMeteorCrawler
from src.data_crawler.fao_agri_api import FaoAgriCrawler
from src.data_crawler.soil_nutrient_spider import SoilNutrientSpider
from src.data_crawler.pest_market_spider import PestMarketSpider
from src.data_crawler.remote_sense_parser import RemoteSenseParser

from src.data_process.data_clean import DataCleaner
from src.data_process.data_fusion import DataFusionCleaner
from src.data_process.data_normalize import DataNormalizer
from src.data_process.dataset_split import TimeSeriesDatasetSplitter

from src.model.cnn_transformer import CNNTransformerAgriculture
from src.train.trainer import DeepTrainer
from src.train.metric import calc_rmse, calc_mae, calc_r2

from src.algorithm.nsga2_moo import RiceCrabNSGA2
from src.algorithm.uav_ga_path import UAVPathPlanner
from src.algorithm.risk_assessor import RiceCrabRiskAssessor

from src.visual.plot_loss_curve import plot_loss_curve
from src.visual.plot_metric_curve import plot_metric_curve
from src.visual.plot_pareto import plot_pareto_front
from src.visual.plot_uav_path import plot_uav_route

from src.utils.logger import logger
from src.utils.report_export import export_full_report
import torch
import pandas as pd
import numpy as np

def main():
    logger.info("========== 稻蟹智能数字孪生系统启动 ==========")
    logger.info("系统模式：纯联网真实官方数据，无仿真、无离线兜底")
    # 1.多源数据采集
    logger.info("1. 采集NASA、FAO、土壤、病虫害、遥感NDVI数据")
    nasa_df = NasaMeteorCrawler().fetch_10year_meteor()
    fao_df = FaoAgriCrawler().fetch_rice_crab_stat()
    soil_df = SoilNutrientSpider().fetch_soil_benchmark()
    pest_df = PestMarketSpider().fetch_pest_market_data()
    ndvi_df = RemoteSenseParser().parse_ndvi_dataset(nasa_df)
    # 2.数据清洗
    logger.info("2. 多源数据清洗标准化")
    cleaner = DataCleaner()
    nasa_clean = cleaner.full_clean_pipeline(nasa_df)
    soil_clean = cleaner.full_clean_pipeline(soil_df)
    pest_clean = cleaner.full_clean_pipeline(pest_df)
    ndvi_clean = cleaner.full_clean_pipeline(ndvi_df)
    fusion_df = DataFusionCleaner().merge_all_source_data(nasa_clean, soil_clean, pest_clean, ndvi_clean)
    # 3.归一化与时序数据集划分
    logger.info("3. 数据归一化，构建训练/验证/测试时序数据集")
    normalizer = DataNormalizer()
    scaled_df = normalizer.fit_transform_data(fusion_df)
    train_set, val_set, test_set = TimeSeriesDatasetSplitter().build_sequence_dataset(scaled_df)
    # 4.模型训练与测试评估
    logger.info("4. CNN-Transformer模型训练")
    model = CNNTransformerAgriculture()
    trainer = DeepTrainer(model, train_set, val_set, test_set)
    train_loss, val_loss, r2_list, mae_list = trainer.full_train()
    x_test, y_test = test_set
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.eval()
    with torch.no_grad():
        pred_test = model(torch.tensor(x_test).to(device)).cpu().numpy()
    y_test_flat = y_test[:, -1, :]
    test_r2 = calc_r2(pred_test, y_test_flat)
    test_mae = calc_mae(pred_test, y_test_flat)
    test_rmse = calc_rmse(pred_test, y_test_flat)
    model_metric = {
        "测试集R²": round(test_r2,4),
        "测试集MAE": round(test_mae,4),
        "测试集RMSE": round(test_rmse,4)
    }
    logger.info(f"模型测试集指标：{model_metric}")
    # 5.智能优化算法
    logger.info("5. NSGA-II多目标种养优化")
    pareto_res = RiceCrabNSGA2().run_optimization()
    logger.info("6. GA无人机巡检路径规划")
    uav_planner = UAVPathPlanner()
    best_route, best_dist = uav_planner.gen_best_route()
    logger.info("7. 多维度种养风险评估")
    risk_res = RiceCrabRiskAssessor().full_risk_evaluate(pest_clean, nasa_clean, fao_df, ndvi_clean)
    logger.info(f"综合风险评估结果：{risk_res}")
    # 6.生成全部可视化图表
    logger.info("8. 自动绘制全部分析图表")
    plot_loss_curve(train_loss, val_loss)
    plot_metric_curve(r2_list, mae_list)
    plot_pareto_front(pareto_res)
    plot_uav_route(best_route, best_dist)
    # 7.导出完整Excel分析报告
    logger.info("9. 导出系统完整分析报告")
    data_stat = {
        "总原始样本量": len(fusion_df),
        "训练集样本": len(train_set[0]),
        "验证集样本": len(val_set[0]),
        "测试集样本": len(test_set[0])
    }
    export_full_report(data_stat, model_metric, pareto_res, risk_res, best_dist)
    logger.info("========== 稻蟹智能数字孪生系统全部流程执行完毕 ==========")

if __name__ == "__main__":
    main()
