#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 15:55:53 2018
@author: jose
"""
from __future__ import division
from os import listdir
from os.path import isfile, join
from matplotlib import pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import pandas as pd
from scipy import stats
from scipy.stats import norm, ks_2samp
from scipy.optimize import curve_fit
from scipy.interpolate import UnivariateSpline
from numpy import linspace
from numpy import log, log10
from numpy import mean, median, std
from numpy import array
from numpy import percentile
import numpy as np
from numpy import sqrt
from numpy import exp
from math import pi
import math
import matplotlib.mlab as mlab
from scipy.stats import chisquare
from scipy.stats import chi2
import random
import sys
import os
from scipy.stats import ks_2samp
from scipy.stats import f_oneway
from scipy.stats import ttest_ind
from scipy.stats import ttest_1samp
from scipy.stats import kruskal
from scipy.stats import mannwhitneyu
from scipy.stats import wilcoxon
from scipy.stats import ranksums
from scipy.stats import friedmanchisquare
from scipy.stats import pearsonr
from scipy.stats import spearmanr
from scipy.stats import pointbiserialr
from scipy.stats import chi2_contingency
import seaborn as sns
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from statsmodels.stats.multicomp import MultiComparison
import statsmodels.stats.api as sms
import statsmodels.stats.power as ssp
import statsmodels.sandbox.stats.runs as ssr
import statsmodels.graphics.boxplots as bp
from statsmodels.graphics.factorplots import interaction_plot
from statsmodels.graphics.mosaicplot import mosaic
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from statsmodels.stats.multicomp import MultiComparison
import statsmodels.stats.api as sms
import statsmodels.stats.power as ssp
import statsmodels.sandbox.stats.runs as ssr
import statsmodels.graphics.boxplots as bp
from statsmodels.graphics.factorplots import interaction_plot
from statsmodels.graphics.mosaicplot import mosaic
import statsmodels.formula.api as smf
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from statsmodels.stats.multicomp import MultiComparison
import statsmodels.stats.api as sms
import statsmodels.stats.power as ssp
import statsmodels.sandbox.stats.runs as ssr
import statsmodels.graphics.boxplots as bp
from statsmodels.graphics.factorplots import interaction_plot
from statsmodels.graphics.mosaicplot import mosaic
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import sys
import os
def main():
    n = int(sys.stdin.readline())
    times = []
    distances = []
    for i in range(n):
        [t, d] = [int(x) for x in sys.stdin.readline().split()]
        times.append(t)
        distances.append(d)
    #print(times)
    #print(distances)
    speeds = [0 for x in range(n)]
    for i in range(n-1):
        speeds[i] = (distances[i+1] - distances[i]) / (times[i+1] - times[i])
    #print(speeds)
    print(int(max(speeds))) 
if __name__ == '__main__':
    main()
