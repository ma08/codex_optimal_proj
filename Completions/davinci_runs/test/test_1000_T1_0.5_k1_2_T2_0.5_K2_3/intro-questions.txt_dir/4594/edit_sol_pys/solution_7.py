# -*- coding: utf-8 -*-
import sys
import numpy as np
from scipy.optimize import curve_fit

# データファイル読み込み
data = np.loadtxt("data.txt")

# 初期値
initial_guess = [1.0, 1.0]

# フィッティング
popt, pcov = curve_fit(func, xdata, ydata, initial_guess)
print(popt)
