#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division, print_function, absolute_import
import sys
import os
import numpy as np
import cv2
import glob
import pickle
import time
import argparse
import matplotlib.pyplot as plt
import pandas as pd
from tqdm import tqdm
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.externals import joblib




n = int(input())
a = [int(x) for x in input().split()]

def solve(a):
    n = len(a)
    dp = [[0, 0] for _ in range(n)]
    dp[0][0] = 1
    dp[0][1] = 1
    for i in range(1, n):
        if a[i] > a[i - 1]:
            dp[i][0] = max(dp[i - 1][0] + 1, dp[i - 1][1] + 1)
            dp[i][1] = dp[i - 1][1] + 1
        else:
            dp[i][0] = dp[i - 1][0] + 1
            dp[i][1] = max(dp[i - 1][0] + 1, dp[i - 1][1] + 1)
    return max(dp[n - 1][0], dp[n - 1][1])

print(solve(a))
