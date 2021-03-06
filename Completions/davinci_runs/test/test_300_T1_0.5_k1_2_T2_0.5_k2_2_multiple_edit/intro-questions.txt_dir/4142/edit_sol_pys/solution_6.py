
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 23:55:54 2020
@author: yuzhang
"""
import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from scipy.stats import norm
from scipy.stats import ttest_1samp
from scipy.stats import ttest_ind
from scipy.stats import ttest_rel
from statsmodels.stats.power import ttest_power
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from statsmodels.stats.multicomp import MultiComparison
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
from statsmodels.graphics.regressionplots import *
from statsmodels.graphics.factorplots import interaction_plot
from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.stats.diagnostic import het_breuschpagan
from statsmodels.stats.diagnostic import het_white
from statsmodels.stats.diagnostic import het_goldfeldquandt
from statsmodels.stats.diagnostic import het_arch
from statsmodels.stats.stattools import durbin_watson
from statsmodels.stats.stattools import jarque_bera
from statsmodels.stats.stattools import omni_normtest
from statsmodels.stats.stattools import levene
from statsmodels.stats.stattools import shapiro
from statsmodels.stats.stattools import kstest
from statsmodels.stats.stattools import sms
from statsmodels.stats.stattools import coint
from statsmodels.stats.stattools import kpss
from statsmodels.stats.stattools import adfuller
from statsmodels.stats.stattools import q_stat
from statsmodels.stats.stattools import grangercausalitytests
from statsmodels.stats.stattools import acorr_ljungbox
from statsmodels.stats.stattools import acf
from statsmodels.stats.stattools import pacf
from statsmodels.stats.stattools import medcouple
from statsmodels.stats.stattools import het_breuschpagan
from statsmodels.stats.stattools import het_white
from statsmodels.stats.stattools import het_goldfeldquandt
from statsmodels.stats.stattools import het_arch
from statsmodels.stats.stattools import het_breushpagan
from statsmodels.stats.stattools import het_white
from statsmodels.stats.stattools import het_goldfeldquandt
from statsmodels.stats.stattools import het_arch
from statsmodels.stats.stattools import het_breushpagan
from statsmodels.stats.stattools import het_white
from statsmodels.stats.stattools import het_goldfeldquandt
from statsmodels.stats.stattools import het_arch
from statsmodels.stats.stattools import het_breushpagan
from statsmodels.stats.stattools import het_white
from statsmodels.stats.stattools import het_goldfeldquandt
from statsmodels.stats.stattools import het_arch
from statsmodels.stats.stattools import het_breushpagan
from statsmodels.stats.stattools import het_white
from statsmodels.stats.stattools import het_goldfeldquandt
from statsmodels.stats.stattools import het_arch
from statsmodels.stats.stattools import het_breushpagan
from statsmodels.stats.stattools import het_white
from statsmodels.stats.stattools import het_goldfeldquandt
from statsmodels.stats.stattools import het_arch
from statsmodels.stats.stattools import het_breushpagan
from statsmodels.stats.stattools import het_white
from statsmodels.stats.stattools import het_goldfeldquandt
from statsmodels.stats.stattools import het_arch
from statsmodels.stats.stattools import het_breushpagan
from statsmodels.stats.stattools import het_white
from statsmodels.stats.stattools import het_goldfeldquandt
from statsmodels.stats.stattools import het_arch
from statsmodels.stats.stattools import het_breushpagan
from statsmodels.stats.stattools import het_white
from statsmodels.stats.stattools import het_goldfeldquandt
from statsmodels.stats.stattools import het_arch
from statsmodels.stats.stattools import het_breushpagan
from statsmodels.stats.stattools import het_white
from statsmodels.stats.stattools import het_goldfeldquandt
from statsmodels.stats.stattools import het_arch
from statsmodels.stats.stattools import het_breushpagan
from statsmodels.stats.stattools import het_white
from statsmodels.stats.stattools import het_goldfeldquandt
from statsmodels.stats.stattools import het_arch
from statsmodels.stats.stattools import het_breushpagan
from statsmodels.stats.stattools import het_white
from statsmodels.stats.stattools import het_goldfeldquandt
from statsmodels.stats.stattools import het_arch
from statsmodels.stats.stattools import het_breushpagan
from statsmodels.stats.stattools import het_white
from statsmodels.stats.stattools import het_goldfeldquandt
from statsmodels.stats.stattools import het_arch
from statsmodels.stats.stattools import het_breushpagan
from statsmodels.stats.stattools import het_white
from statsmodels.stats.stattools import het_goldfeldquandt
from statsmodels.stats.stattools import het_arch
from statsmodels.stats.stattools import het_breushpagan
from statsmodels.stats.stattools import het_white
from statsmodels.stats.stattools import het_goldfeldquandt
from statsmodels.stats.stattools import het_arch
from statsmodels.stats.stattools import het_breushpagan
from statsmodels.stats.stattools import het_white
from statsmodels.stats.stattools import het_goldfeldquandt
from statsmodels.stats.stattools import het_arch
from statsmodels.stats.stattools import het_breushpagan
from statsmodels.stats.stattools import het_white
from statsmodels.stats.stattools import het_goldfeldquandt
from statsmodels.stats.stattools import het_arch
from statsmodels.stats.stattools import het_breushpagan
from statsmodels.stats.stattools import het_white
from statsmodels.stats.stattools import het_goldfeldquandt
from statsmodels.stats.stattools import het_arch
from statsmodels.stats.stattools import het_breushpagan
from statsmodels.stats
