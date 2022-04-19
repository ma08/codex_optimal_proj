#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 14:51:53 2018


@author: kazuki.onodera
"""


import numpy as np
import pandas as pd
import os
from glob import glob
from tqdm import tqdm

import sys
sys.path.append(f'/home/{os.environ.get("USER")}/PythonLibrary')
import lgbextension as ex
import lightgbm as lgb
from multiprocessing import cpu_count

from sklearn.model_selection import GroupKFold
from sklearn.metrics import roc_auc_score

import utils
utils.start(__file__)
#==============================================================================

SEED = np.random.randint(9999)
print('SEED:', SEED)

NFOLD = 5

LOOP = 5

param = {
         'objective': 'binary',
         'metric': 'auc',
         'learning_rate': 0.01,
         'max_depth': -1,
         'num_leaves': 255,
         'max_bin': 255,
         'colsample_bytree': 0.5,
         'subsample': 0.5,
         'nthread': 32,
         'bagging_freq': 1,
#         'verbose':-1,
         }


# =============================================================================
# load
# =============================================================================
X_train = pd.read_feather('../data/X_train.f')
y_train = utils.read_pickles('../data/label').TARGET

# =============================================================================
# cv
# =============================================================================

group_kfold = GroupKFold(n_splits=NFOLD)

models = []
for i in range(LOOP):
    gc.collect()
    param.update({'seed':np.random.randint(9999)})
    model = lgb.LGBMClassifier(**param)
    model.fit(X_train, y_train)
    models.append(model)

del X_train, y_train; gc.collect()

"""

models = []
for i in range(LOOP):
    gc.collect()
    param.update({'seed':np.random.randint(9999)})
    model = lgb.train(param, dtrain, len(X.columns),
                      feval=ex.eval_auc,
                      valid_names=['train','valid'],
                      valid_sets=[dtrain, dvalid],
                      verbose_eval=50,
                      early_stopping_rounds=100)
    models.append(model)

del dtrain, dvalid; gc.collect()

"""

imp = ex.getImp(models)


# =============================================================================
# test
# =============================================================================

files_te = sorted(glob('../data/test_f*.f'))

X_test = pd.concat([
                pd.read_feather(f) for f in tqdm(files_te, mininterval=60)
               ], axis=1)

files_te = sorted(glob('../feature_someone/test_f*.f'))
X_test_ = pd.concat([
                pd.read_feather(f) for f in tqdm(files_te, mininterval=60)
               ], axis=1)

X_test = pd.concat([X_test, X_test_], axis=1)

sub = pd.read_pickle('../data/sub.p')

gc.collect()

label_name = 'TARGET'

sub[label_name] = 0
for model in models:
    y_pred = model.predict_proba(X_test)[:, 1]
    sub[label_name] += pd.Series(y_pred).rank()
sub[label_name] /= LOOP
sub[label_name] /= sub[label_name].max()
sub['SK_ID_CURR'] = sub['SK_ID_CURR'].map(int)

sub.to_csv(SUBMIT_FILE_PATH, index=False, compression='gzip')

# =============================================================================
# submission
# =============================================================================
if EXE_SUBMIT:
    print('submit')
    utils.submit(SUBMIT_FILE_PATH, COMMENT)


#==============================================================================
utils.end(__file__)
