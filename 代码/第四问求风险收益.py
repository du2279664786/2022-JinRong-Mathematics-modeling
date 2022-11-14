#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:杜培博
# datetime:2022/11/7 15:11
# software: PyCharm
import matplotlib.pyplot as plt
from pandas import read_excel
import numpy as np
import pandas  as pd
import scipy.optimize as sco
import warnings
warnings.filterwarnings("ignore")
plt.rcParams['font.sans-serif'] = ['SimHei']  # 中文字体设置-黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
data = pd.read_excel("E:\\File\\数学建模\\第二届“大湾区杯”粤港澳金融数学数学建模竞赛赛题\\2022年题目\\B题\\附件2：大类资产指数行情数据（3、4问）\\大类资产指数行情数据.xlsx")
data = pd.read_excel("E:/预测五年后四类.xlsx")
data

# for i in ['沪深300','南华商品指数','中债-综合财富(3-5年)指数','货币基金']:
#     data[i] = (data[i]-data[i].min())/(data[i].max()-data[i].min())
temp_data = data[['沪深300','南华商品指数','中债-综合财富(3-5年)指数','货币基金']]

# 计算每个特征的收益率
temp_data=np.log(temp_data)-np.log(temp_data.shift(1))
temp_data

temp_data.dropna(inplace=True)
# temp_data = temp_data.iloc[1:,:]
temp_data['货币基金'] = np.sqrt(temp_data['货币基金']+1)
plt_hist=temp_data.hist(figsize=(20,5),grid=False,layout =(1,5))

W=np.array([0.25]*4)
stock_mean=temp_data.mean()*len(temp_data.index)
stock_cov=temp_data.cov()*len(temp_data.index)
r_portfolio=np.dot(stock_mean,W)
var_portfolio=np.dot(W,stock_cov)
var_portfolio=np.dot(var_portfolio,W.T)
sharp_ratio=r_portfolio/var_portfolio
print(sharp_ratio)

def min_sharp_ratio(W):
    W=np.array(W)
    stock_mean=temp_data.mean()*len(temp_data.index)
    stock_cov=temp_data.cov()*len(temp_data.index)
    r_portfolio=np.dot(stock_mean,W) #得到投资组合的期望收益
    var_portfolio=np.dot(W,stock_cov)
    var_portfolio=np.dot(var_portfolio,W.T) #得到投资组合的方差
    return -r_portfolio/var_portfolio  #返回负的夏普比率

cons = ({'type': 'eq', 'fun': lambda W: -np.sum(W) + 1}) #投资组合权重之和为1
bnds = tuple((0, 1) for W in range(len(temp_data.columns)))
W0=np.array([0.25]*4)
temp = sco.minimize(min_sharp_ratio, W0, method='SLSQP', bounds=bnds,constraints=cons)
# opts_sharpratio
def min_var(W):
    W=np.array(W)
    stock_mean=temp_data.mean()*len(temp_data.index)
#     stock_co
    v=temp_data.cov()*len(temp_data.index)
    r_portfolio=np.dot(stock_mean,W) #得到投资组合的期望收益
#     print('组合投资的期望收益：',r_portfolio)
    var_portfolio=np.dot(W,stock_cov)
    var_portfolio=np.dot(var_portfolio,W.T) #得到投资组合的方差
#     print('组合投资的方差：',var_portfolio)
    return var_portfolio  #返回投资组合方差
opts_var = sco.minimize(min_var, W0, method='SLSQP', bounds=bnds,constraints=cons)
print(opts_var['x'].round(3))

