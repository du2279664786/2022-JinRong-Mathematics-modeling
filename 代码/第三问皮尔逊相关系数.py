#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:杜培博
# datetime:2022/11/7 14:59
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

data = pd.read_excel("E:\\File\\数学建模\\第二届“大湾区杯”粤港澳金融数学数学建模竞赛赛题\\2022年题目\\B题\\附件2：大类资产指数行情数据（3、4问）\\大类资产指数行情数据.xlsx")

result = data.corr(method='pearson')
result.index = data.corr(method='pearson').index
mask = np.zeros_like(result, dtype=np.bool)   #定义一个大小一致全为零的矩阵  用布尔类型覆盖原来的类型
mask[np.triu_indices_from(result)]= True      #返回矩阵的上三角，并将其设置为true
plt.figure(figsize=(16,13))
# cmap = sns.choose_diverging_palette()
cmap = sns.diverging_palette(230, 20, as_cmap=True)
sns.heatmap(result,square=True, cmap=cmap,mask=mask,fmt='.2f',annot=True)
plt.savefig('E:/photo/第三问相关性')

