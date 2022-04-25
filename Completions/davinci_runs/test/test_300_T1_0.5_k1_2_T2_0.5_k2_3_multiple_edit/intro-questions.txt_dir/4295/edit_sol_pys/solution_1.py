#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/kazuki/Documents/Study/data/ryukyu/kumamoto.csv')

plt.plot(df['year'], df['max'])
plt.plot(df['year'], df['min'])
plt.show()
