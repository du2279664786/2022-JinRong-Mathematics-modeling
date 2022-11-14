#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:杜培博
# datetime:2022/11/7 14:53
# software: PyCharm
# Feature Extraction with PCA
import numpy
from pandas import read_csv
from sklearn.decomposition import PCA
import pandas as pd
import seaborn as sns
import numpy as np
import pandas as pd
from factor_analyzer import FactorAnalyzer
from sklearn.datasets import load_breast_cancer
cancer = load_breast_cancer()
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")
plt.rcParams['font.sans-serif'] = ['SimHei']  # 中文字体设置-黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

# 数据的读取 包含：CPI 	PPI 	GDP 	大宗商品价格指数 	广义货币供应量
gdp = pd.read_excel("E:\\File\\数学建模\\第二届“大湾区杯”粤港澳金融数学数学建模竞赛赛题\\2022年题目\\B题\\data.xlsx")

gdp['mon'] = gdp['date'].dt.month
gdp['date'] = gdp['date'].dt.year
train =gdp[gdp['num'].notnull()]
test = gdp[gdp['num'].isnull()]

from statsmodels.tsa.stattools import adfuller
a = train['num']
print(adfuller(a,    # 下述参数均为默认值
				maxlag=None,
				regression='c',
				autolag='AIC',   # 自动在[0, 1,...,maxlag]中间选择最优lag数的方法；
				store=False,
				regresults=False)
				)

[t, p, c, r] = adfuller(x=a, regression='ctt', regresults=True)
print("r.resols.summary() is")
print(r.resols.summary())



# ARIMA 模型
from statsmodels.tsa.arima.model import ARIMA
data = train['num'][-20:]
model = ARIMA(data, order=(0, 2, 0))
model_fit = model.fit()       # 训练
yhat = model_fit.predict(68)    # 预测
print(yhat)