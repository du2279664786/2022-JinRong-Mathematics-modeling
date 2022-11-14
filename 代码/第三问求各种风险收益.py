#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:杜培博
# datetime:2022/11/7 15:07
# software: PyCharm
# Feature Extraction with PCA
import numpy
from pandas import read_csv
from sklearn.decomposition import PCA
import pandas as pd
import math
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


data = pd.read_excel("E:\\File\\数学建模\\第二届“大湾区杯”粤港澳金融数学数学建模竞赛赛题\\2022年题目\\B题\\附件2：大类资产指数行情数据（3、4问）\\大类资产指数行情数据.xlsx")

data[['沪深300','南华商品指数','中债-综合财富(3-5年)指数','货币基金']].plot()

# 计算各种收益
def recwve(data):
    for j in [i for i in data.columns.tolist()]:
        print(j + '的日收益率为：', np.mean(data[j]))
        print(j + '的收益率的标准差为：', data[j].std())
        mm = np.mean(data[j])
        nn = data[j].std()
        ss = mm - 0.01059015326852
        SR = ss / nn
        print(j + '的日夏普比率为：', SR)
        SR1 = (mm - 0.01059015326852) / nn * math.sqrt(252)
        print(j + '的年夏普比率为：', SR1)
        min_periods = 12
        # 计算波动率
        vol = data[j].rolling(min_periods).std() * np.sqrt(min_periods)

        print(j + '波动率为：', np.mean(vol))


recwve(data[['沪深300', '南华商品指数', '中债-综合财富(3-5年)指数', '货币基金']])


min_periods = 12
# 计算波动率
vol = data['沪深300'].rolling(min_periods).std() * np.sqrt(min_periods)
np.mean(vol)

# 衰退
def recwve(data):
    for j in [i for i in data.columns.tolist()]:
        print(j + '的日收益指数为：', np.mean(data[j]))
        print(j + '的收益率的标准差为：', data[j].std())
        mm = np.mean(data[j])
        nn = data[j].std()
        ss = mm - 0.01059015326852
        SR = ss / nn
        print(j + '的日夏普比率为：', SR)
        SR1 = (mm - 0.01059015326852) / nn * math.sqrt(252)
        #         print(j+'的年夏普比率为：',SR1)
        min_periods = 12
        # 计算波动率
        vol = data[j].rolling(min_periods).std() * np.sqrt(min_periods)

        print(j + '波动率为：', np.mean(vol))


recwve(data[['沪深300', '南华商品指数', '中债-综合财富(3-5年)指数', '货币基金']])

# 过热

data = pd.read_excel("E:/过热.xlsx")


def recwve(data):
    for j in [i for i in data.columns.tolist()]:
        print(j + '的日收益指数为：', np.mean(data[j]))
        print(j + '的收益率的标准差为：', data[j].std())
        mm = np.mean(data[j])
        nn = data[j].std()
        ss = mm - 0.01059015326852
        SR = ss / nn
        print(j + '的日夏普比率为：', SR)
        SR1 = (mm - 0.01059015326852) / nn * math.sqrt(252)
        #         print(j+'的年夏普比率为：',SR1)
        min_periods = 12
        # 计算波动率
        vol = data[j].rolling(min_periods).std() * np.sqrt(min_periods)

        print(j + '波动率为：', np.mean(vol))


recwve(data[['沪深300', '南华商品指数', '中债-综合财富(3-5年)指数', '货币基金']])

# 复苏

data = pd.read_excel("E:/复苏.xlsx")


def recwve(data):
    for j in [i for i in data.columns.tolist()]:
        print(j + '的日收益指数为：', np.mean(data[j]))
        print(j + '的收益率的标准差为：', data[j].std())
        mm = np.mean(data[j])
        nn = data[j].std()
        ss = mm - 0.01059015326852
        SR = ss / nn
        print(j + '的日夏普比率为：', SR)
        SR1 = (mm - 0.01059015326852) / nn * math.sqrt(252)
        #         print(j+'的年夏普比率为：',SR1)
        min_periods = 12
        # 计算波动率
        vol = data[j].rolling(min_periods).std() * np.sqrt(min_periods)

        print(j + '波动率为：', np.mean(vol))


recwve(data[['沪深300', '南华商品指数', '中债-综合财富(3-5年)指数', '货币基金']])

# 滞涨
data = pd.read_excel("E:/滞胀.xlsx")


def recwve(data):
    for j in [i for i in data.columns.tolist()]:
        print(j + '的日收益指数为：', np.mean(data[j]))
        print(j + '的收益率的标准差为：', data[j].std())
        mm = np.mean(data[j])
        nn = data[j].std()
        ss = mm - 0.01059015326852
        SR = ss / nn
        print(j + '的日夏普比率为：', SR)
        SR1 = (mm - 0.01059015326852) / nn * math.sqrt(252)
        #         print(j+'的年夏普比率为：',SR1)
        min_periods = 12
        # 计算波动率
        vol = data[j].rolling(min_periods).std() * np.sqrt(min_periods)

        print(j + '波动率为：', np.mean(vol))


recwve(data[['沪深300', '南华商品指数', '中债-综合财富(3-5年)指数', '货币基金']])