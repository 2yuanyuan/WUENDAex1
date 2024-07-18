import numpy as np
# 主要对多维数组执行计算（矩阵、数组运算的基础）
# 便于数值计算
import pandas as pd
# 通常用途相当于excel，对数据进行变换
import matplotlib.pyplot as plt
# 用于绘图的一个库
A= np.identity(5)
#实际上np.identity(5)也可以
print(A)
path='ex1data1.txt'
data=pd.read_csv(path,header=None,names=['Population','Profit'])
#header 设置几，则表头从数据中第几行开始抽取
#names 通常用于数据表没有表头的时候，手动指定表头
#实际上names赋值后header会自动赋none
data.head() #数据预览
