import numpy as np
import pandas as pd

class RiceCrabRiskAssessor:
    def __init__(self):
        self.weight = {
            "pest_risk": 0.35,
            "climate_risk": 0.3,
            "cost_risk": 0.2,
            "growth_risk": 0.15
        }

    def calc_pest_risk(self, pest_data):
        base = np.clip(pest_data["pest_rate"].values, 0, 1)
        return base * 100

    def calc_climate_risk(self, weather_data):
        temp_abnormal = np.abs(weather_data["temp"] - 25) / 10
        rain_abnormal = np.abs(weather_data["rainfall"] - 80) / 50
        return np.clip((temp_abnormal + rain_abnormal) * 50, 0, 100)

    def calc_cost_risk(self, cost_data):
        cost_std = np.std(cost_data["input_cost"])
        cost_mean = np.mean(cost_data["input_cost"])
        risk = (cost_std / (cost_mean + 1e-6)) * 100
        return np.clip(risk, 0, 100)

    def calc_growth_risk(self, ndvi_data):
        ndvi_mean = np.mean(ndvi_data["ndvi"])
        risk = (1 - ndvi_mean) * 100
        return np.clip(risk, 0, 100)

    def full_risk_evaluate(self, pest_df, weather_df, cost_df, ndvi_df):
        pest_r = self.calc_pest_risk(pest_df)
        climate_r = self.calc_climate_risk(weather_df)
        cost_r = self.calc_cost_risk(cost_df)
        growth_r = self.calc_growth_risk(ndvi_df)
        total_risk = (
            self.weight["pest_risk"] * np.mean(pest_r) +
            self.weight["climate_risk"] * np.mean(climate_r) +
            self.weight["cost_risk"] * cost_r +
            self.weight["growth_risk"] * growth_r
        )
        if total_risk < 30:
            level = "低风险"
        elif total_risk < 60:
            level = "中风险"
        else:
            level = "高风险"
        return {
            "total_risk_score": round(total_risk, 2),
            "risk_level": level,
            "pest_risk_score": round(np.mean(pest_r), 2),
            "climate_risk_score": round(np.mean(climate_r), 2),
            "cost_risk_score": round(cost_r, 2),
            "growth_risk_score": round(growth_r, 2)
        }
