import pandas as pd
import numpy as np
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.stattools import adfuller
import warnings
warnings.filterwarnings("ignore")

class ARIMATimeSeriesPredict:
    def __init__(self):
        self.best_order = (2,1,1)

    def check_stationary(self, ts_data):
        adf_res = adfuller(ts_data)
        return adf_res[1] < 0.05

    def find_best_order(self, ts_data):
        best_aic = float("inf")
        best_order = (2,1,1)
        for p in range(3):
            for q in range(3):
                try:
                    model = ARIMA(ts_data, order=(p,1,q))
                    res = model.fit()
                    if res.aic < best_aic:
                        best_aic = res.aic
                        best_order = (p,1,q)
                except:
                    continue
        self.best_order = best_order
        return best_order

    def predict_future(self, ts_data, future_step=30):
        self.find_best_order(ts_data)
        model = ARIMA(ts_data, order=self.best_order)
        fit_res = model.fit()
        pred = fit_res.get_forecast(steps=future_step)
        pred_mean = pred.predicted_mean
        pred_ci = pred.conf_int()
        return pred_mean.values, pred_ci
