#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:杜培博
# datetime:2022/11/7 14:49
# software: PyCharm
import pandas as pd
from sklearn import svm
from sklearn.linear_model import LinearRegression
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import seaborn as sns
plt.rcParams['font.sans-serif'] = ['SimHei']  # 中文字体设置-黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
# sns.set(font='SimHei',font_scale=1.5)  # 解决Seaborn中文显示问题并调整字体大小
import warnings
warnings.filterwarnings('ignore')

data = pd.read_excel("E:\\File\\数学建模\\第二届“大湾区杯”粤港澳金融数学数学建模竞赛赛题\\2022年题目\\B题\\附件1：宏观经济指标数据（1、2问）\\合计特征的数据.xlsx")

# 归一化
for i in ['CPI','PPI','GDP','大宗商品价格指数','广义货币供应量']:
    data[i] = (data[i]-data[i].min())/(data[i].max()-data[i].min())

result = data.corr()
result.index = data.corr(method='pearson').index
mask = np.zeros_like(result, dtype=np.bool)   #定义一个大小一致全为零的矩阵  用布尔类型覆盖原来的类型
mask[np.triu_indices_from(result)]= True      #返回矩阵的上三角，并将其设置为true
plt.figure(figsize=(16,13))
# cmap = sns.choose_diverging_palette()
cmap = sns.diverging_palette(230, 20, as_cmap=True)
sns.heatmap(result,square=True, cmap=cmap,mask=mask,fmt='.2f',annot=True)
plt.savefig('E:/photo/第一问求相关性')