

# Import
import sys
import heapq
import collections
import bisect
import random
import fractions
import copy
import functools
import itertools
import pprint
import numpy as np
import scipy as sp
import scipy.misc
import scipy.ndimage
import scipy.optimize
import scipy.stats
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import networkx as nx
import pandas as pd
import tqdm
import sklearn
import sklearn.decomposition
import sklearn.metrics
import sklearn.cluster
import sklearn.datasets
import sklearn.manifold
import sklearn.neighbors
import sklearn.ensemble
import sklearn.tree
import sklearn.svm
import sklearn.discriminant_analysis
import sklearn.naive_bayes
import sklearn.linear_model
import sklearn.multiclass
import sklearn.neural_network
import sklearn.pipeline
import sklearn.preprocessing
import math

# Functions
def input():
    return sys.stdin.readline().strip()

# Main
N = int(input())
d = list(map(int, input().split()))

# Sorting
d.sort()

# Number of problems
count = 0

# Solve
for i in range(N//2):
    if d[i] == d[N//2]:
        count += 1
    elif d[i] < d[N//2]:
        break

print(count)
