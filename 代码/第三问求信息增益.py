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


# 包含特征；时间 	上证50 	沪深300 	中证500 	中证1000 	南华商品指数 	标普高盛商品全收益指数 	中债-综合财富(1年以下)指数 	中债-综合财富(3-5年)指数 	中债-综合财富(7-10年)指数 	货币基金
data = pd.read_excel("E:\\File\\数学建模\\第二届“大湾区杯”粤港澳金融数学数学建模竞赛赛题\\2022年题目\\B题\\附件2：大类资产指数行情数据（3、4问）\\大类资产指数行情数据.xlsx")

# 函数实现相关性分析

# 信息熵
def info_entropy(attr):
    prob = pd.value_counts(attr) / len(attr)   # 对于一个特征不同类所占的比例类
    return sum( np.log2( prob )* prob * (-1) )  # 经验熵


def infor(data):
    a = pd.value_counts(data) / len(data)
#     print('信息熵：',sum(np.log2(a) * a * (-1)))
    return sum(np.log2(a) * a * (-1))

# 定义计算信息增益的函数：计算g(D|A)
def g(data, str1, str2):
    e1 = data.groupby(str1).apply(lambda x: infor(x[str2]))
    p1 = pd.value_counts(data[str1]) / len(data[str1])
    # 计算Infor(D|A)
    e2 = sum(e1 * p1)
    return infor(data[str2]) - e2

def cor(data):
    pca = PCA(n_components=1)
    pca.fit(gupiao)
    X_new = pca.transform(gupiao)
    data['label'] = X_new
    for j in [i for i in data.columns.tolist() if i!='label']:
        for i in ['label']:
            print(str(j)+'和'+str(i)+'特征的信息增益:'+str(g(data,j, i)/np.sqrt(info_entropy(data[i])*round(info_entropy(data[j]),4))))


# 故票
gupiao = data[['上证50','沪深300','中证500','中证1000']]
cor(gupiao)

# 大宗商品
shangpin = data[['南华商品指数','标普高盛商品全收益指数']]
cor(shangpin)

# 债券
zhiajuan = data[['中债-综合财富(1年以下)指数','中债-综合财富(3-5年)指数','中债-综合财富(7-10年)指数']]
cor(zhiajuan)

