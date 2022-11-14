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
from sklearn.decomposition import PCA
gupiao = data[['上证50','沪深300','中证500','中证1000']]

# 降维到二维
pca = PCA(n_components=1)
pca.fit(gupiao)
# 输出特征值
print(pca.explained_variance_)
# 输出特征向量
print(pca.components_)
# 降维后的数据
X_new = pca.transform(gupiao)
gupiao['label'] = X_new
print(X_new.shape)


# 信息熵
def info_entropy(attr):
    prob = pd.value_counts(attr) / len(attr)   # 对于一个特征不同类所占的比例类
    return sum( np.log2( prob )* prob * (-1) )  # 经验熵

for i in ['上证50','沪深300','中证500','中证1000']:
    print(str(i)+'特征的信息熵:'+str(round(info_entropy(gupiao[i]),4)))

# 商品
shangpin = data[['南华商品指数','标普高盛商品全收益指数']]
# 载入两个检验
from factor_analyzer.factor_analyzer import calculate_bartlett_sphericity,calculate_kmo
chi_square_value, p_value = calculate_bartlett_sphericity(data[['上证50','沪深300','中证500','中证1000']])
chi_square_value,p_value

from factor_analyzer.factor_analyzer import calculate_kmo
kmo_all, kmo_model = calculate_kmo(data[['上证50','沪深300','中证500','中证1000']])
print(kmo_model)

df = data[['上证50','沪深300','中证500','中证1000']]
fa = FactorAnalyzer(1,rotation=None)
fa.fit(df)

ev,v = fa.get_eigenvalues()


# 可视化
# plot横轴是指标个数，纵轴是ev值
# scatter横轴是指标个数，纵轴是ev值

plt.scatter(range(1,df.shape[1]+1),ev)
plt.plot(range(1,df.shape[1]+1),ev)
plt.title('Scree Plot')
plt.xlabel('Factors')
plt.ylabel('Eigenvalue')
plt.grid()
plt.show()

