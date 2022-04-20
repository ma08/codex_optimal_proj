

import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.stats import linregress

# ファイルからデータを読み込み
data = np.loadtxt("data.txt", comments="#", delimiter="\t", unpack=False)

x = data[:,0]
y = data[:,1]

# 線形回帰
slope, intercept, r_value, p_value, std_err = linregress(x,y)

# 係数
a = slope
b = intercept

# 回帰直線
y_fit = a * x + b

# 標準偏差
s = np.sqrt(np.sum((y - y_fit)**2) / (len(x) - 2))

# 偏差平方和
s_s = np.sum((y - y_fit)**2)

# 決定係数
r2 = r_value**2

# 自由度
df = len(x) - 2

# 相関係数
r = np.sqrt(r2)

# 回帰直線の表示
plt.plot(x, y_fit, color="red", linewidth=1)

# 散布図の表示
plt.scatter(x, y, color="blue", marker="o", linewidth=1)

# グラフの表示
plt.show()
