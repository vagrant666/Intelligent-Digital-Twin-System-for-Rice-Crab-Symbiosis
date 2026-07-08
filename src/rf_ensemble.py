"""
随机森林集成评估基准模型
"""
from sklearn.ensemble import RandomForestRegressor
import numpy as np

class RFEnsembleModel:
    def __init__(self):
        self.rf1 = RandomForestRegressor(n_estimators=100, random_state=42)
        self.rf2 = RandomForestRegressor(n_estimators=100, random_state=42)

    def fit(self, x_train, y_train):
        x_flat = x_train.reshape(x_train.shape[0], -1)
        self.rf1.fit(x_flat, y_train[:,0])
        self.rf2.fit(x_flat, y_train[:,1])

    def predict(self, x):
        x_flat = x.reshape(x.shape[0], -1)
        p1 = self.rf1.predict(x_flat)
        p2 = self.rf2.predict(x_flat)
        return np.stack([p1,p2], axis=1)
