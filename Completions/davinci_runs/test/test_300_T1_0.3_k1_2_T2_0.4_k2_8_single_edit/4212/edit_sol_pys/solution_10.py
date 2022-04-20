# -*- coding: utf-8 -*-
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../../'))
from koshort.datasets import load_movie_review
from koshort.preprocessing import Tokenizer
from koshort.preprocessing import Normalizer
from koshort.preprocessing import PadSequence
from koshort.preprocessing import WordEmbedding
from koshort.preprocessing import LabelEncoder
from koshort.preprocessing import OneHotEncoder
from koshort.preprocessing import TextVectorization
from koshort.preprocessing import Dataset
from koshort.preprocessing import DataLoader
from koshort.preprocessing import Pipeline
from koshort.preprocessing import FeatureUnion
from koshort.preprocessing import FunctionTransformer
from koshort.preprocessing import StandardScaler
from koshort.preprocessing import MinMaxScaler
from koshort.preprocessing import MaxAbsScaler
from koshort.preprocessing import RobustScaler
from koshort.preprocessing import Normalizer
from koshort.preprocessing import QuantileTransformer
from koshort.preprocessing import PowerTransformer
from koshort.preprocessing import PolynomialFeatures
from koshort.preprocessing import TruncatedSVD
from koshort.preprocessing import PCA
from koshort.preprocessing import KernelPCA
from koshort.preprocessing import FastICA
from koshort.preprocessing import FactorAnalysis
from koshort.preprocessing import SparsePCA
from koshort.preprocessing import MiniBatchDictionaryLearning
from koshort.preprocessing import DictionaryLearning
from koshort.preprocessing import IncrementalPCA
from koshort.preprocessing import NMF
from koshort.preprocessing import LatentDirichletAllocation
from koshort.preprocessing import TruncatedSVD
from koshort.preprocessing import SelectKBest
from koshort.preprocessing import SelectPercentile
from koshort.preprocessing import SelectFpr
from koshort.preprocessing import SelectFdr
from koshort.preprocessing import SelectFwe
from koshort.preprocessing import GenericUnivariateSelect
from koshort.preprocessing import RFE
from koshort.preprocessing import RFECV
from koshort.preprocessing import SelectFromModel
from koshort.preprocessing import SelectFromModel
from koshort.preprocessing import VarianceThreshold
from koshort.preprocessing import SelectPercentile
from koshort.preprocessing import SelectFpr
from koshort.preprocessing import SelectFdr
from koshort.preprocessing import SelectFwe
from koshort.preprocessing import GenericUnivariateSelect
from koshort.preprocessing import RFE
from koshort.preprocessing import RFECV
from koshort.preprocessing import SelectFromModel
from koshort.preprocessing import SelectFromModel
from koshort.preprocessing import VarianceThreshold
from koshort.preprocessing import SelectPercentile
from koshort.preprocessing import SelectFpr
from koshort.preprocessing import SelectFdr
from koshort.preprocessing import SelectFwe
from koshort.preprocessing import GenericUnivariateSelect
from koshort.preprocessing import RFE
from koshort.preprocessing import RFECV
from koshort.preprocessing import SelectFromModel
from koshort.preprocessing import SelectFromModel
from koshort.preprocessing import VarianceThreshold
from koshort.preprocessing import SelectPercentile
from koshort.preprocessing import SelectFpr
from koshort.preprocessing import SelectFdr
from koshort.preprocessing import SelectFwe
from koshort.preprocessing import GenericUnivariateSelect
from koshort.preprocessing import RFE
from koshort.preprocessing import RFECV
from koshort.preprocessing import SelectFromModel
from koshort.preprocessing import SelectFromModel
from koshort.preprocessing import VarianceThreshold
from koshort.preprocessing import SelectPercentile
from koshort.preprocessing import SelectFpr
from koshort.preprocessing import SelectFdr
from koshort.preprocessing import SelectFwe
from koshort.preprocessing import GenericUnivariateSelect
from koshort.preprocessing import RFE
from koshort.preprocessing import RFECV
from koshort.preprocessing import SelectFromModel
from koshort.preprocessing import SelectFromModel
from koshort.preprocessing import VarianceThreshold
from koshort.preprocessing import SelectPercentile
from koshort.preprocessing import SelectFpr
from koshort.preprocessing import SelectFdr
from koshort.preprocessing import SelectFwe
from koshort.preprocessing import GenericUnivariateSelect
from koshort.preprocessing import RFE
from koshort.preprocessing import RFECV
from koshort.preprocessing import SelectFromModel
from koshort.preprocessing import SelectFromModel
from koshort.preprocessing import VarianceThreshold
from koshort.preprocessing import SelectPercentile
from koshort.preprocessing import SelectFpr
from koshort.preprocessing import SelectFdr
from koshort.preprocessing import SelectFwe
from koshort.preprocessing import GenericUnivariateSelect
from koshort.preprocessing import RFE
from koshort.preprocessing import RFECV
from koshort.preprocessing import SelectFromModel
from koshort.preprocessing import SelectFromModel
from koshort.preprocessing import VarianceThreshold
from koshort.preprocessing import SelectPercentile
from koshort.preprocessing import SelectFpr
from koshort.preprocessing import SelectFdr
from koshort.preprocessing import SelectFwe
from koshort.preprocessing import GenericUnivariateSelect
from koshort.preprocessing import RFE
from koshort.preprocessing import RFECV
from koshort.preprocessing import SelectFromModel
from koshort.preprocessing import SelectFromModel
from koshort.preprocessing import VarianceThreshold
from koshort.preprocessing import SelectPercentile
from koshort.preprocessing import SelectFpr
from koshort.preprocessing import SelectFdr
from koshort.preprocessing import SelectFwe
from koshort.preprocessing import GenericUnivariateSelect
from koshort.preprocessing import RFE
from koshort.preprocessing import RFECV
from koshort.preprocessing import SelectFromModel
from koshort.preprocessing import SelectFromModel
from koshort.preprocessing import VarianceThreshold
from koshort.preprocessing import SelectPercentile
from koshort.preprocessing import SelectFpr
from koshort.preprocessing import SelectFdr
from koshort.preprocessing import SelectFwe
from koshort.preprocessing import GenericUnivariateSelect
from koshort.preprocessing import RFE
from koshort.preprocessing import RFECV
from koshort.preprocessing import SelectFromModel
from koshort.preprocessing import SelectFromModel
from koshort.preprocessing import VarianceThreshold
from koshort.preprocessing import SelectPercentile
from koshort.preprocessing import SelectFpr
from koshort.preprocessing import SelectFdr
from koshort.preprocessing import SelectFwe
from koshort.preprocessing import GenericUnivariateSelect
from koshort.preprocessing import RFE
from koshort.preprocessing import RFECV
from koshort.preprocessing import SelectFromModel
from koshort.preprocessing import SelectFromModel
from koshort.preprocessing import VarianceThreshold
from koshort.preprocessing import SelectPercentile
from koshort.preprocessing import SelectFpr
from koshort.preprocessing import SelectFdr
from koshort.preprocessing import SelectFwe
from koshort.preprocessing import GenericUnivariateSelect
from koshort.preprocessing import RFE
from koshort.preprocessing import RFECV

import sys

def main():
    n, m, q = map(int, sys.stdin.readline().split())
    a = [0] * (n + 1)
    for _ in range(q):
        ai, bi, ci, di = map(int, sys.stdin.readline().split())
        a[ai] += di
        a[bi] -= di
    for i in range(1, n + 1):
        a[i] += a[i - 1]
    print(max(a))

if __name__ == '__main__':
    main()
