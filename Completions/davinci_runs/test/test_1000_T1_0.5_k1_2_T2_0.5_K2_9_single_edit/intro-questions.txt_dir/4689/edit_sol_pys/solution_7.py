#!/usr/bin/env python
# -*- coding: utf-8 -*-


import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10, 10, 0.1)
y = np.sin(x)

plt.plot(x, y)
plt.show()
