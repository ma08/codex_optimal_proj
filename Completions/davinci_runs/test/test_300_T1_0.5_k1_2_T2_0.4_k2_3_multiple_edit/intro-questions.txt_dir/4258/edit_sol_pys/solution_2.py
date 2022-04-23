#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 14:07:53 2018

@author: kazuki.onodera
"""

import numpy as np
import pandas as pd
import os, gc
from glob import glob
from tqdm import tqdm

import sys
sys.path.append(f'/home/{os.environ.get("USER")}/PythonLibrary')
import lgbextension as ex
import lightgbm as lgb
from multiprocessing import cpu_count

import utils , utils_cat
utils.start(__file__)
#==============================================================================

SUBMIT_FILE_PATH = '../output/1101-1.csv.gz'

COMMENT = 'nejumi + f001'

EXE_SUBMIT = True

#DROP = ['f001_hostgal_specz']

SEED = np.random.randint(9999)
print('SEED:', SEED)

NFOLD = 5

LOOP = 5

param = {
         'objective': 'multiclass',
         'num_class': 14,
         'metric': 'multi_logloss',
         
         'learning_rate': 0.5,
         'max_depth': 3,
         'num_leaves': 63,
         'max_bin': 255,
         
         'min_child_weight': 10,
         'min_data_in_leaf': 150,
         'reg_lambda': 0.5,  # L2 regularization term on weights.
         'reg_alpha': 0.5,  # L1 regularization term on weights.
         
         'colsample_bytree': 0.5,
         'subsample': 0.5,
#         'nthread': 32,
         'nthread': cpu_count(),
         'bagging_freq': 1,
         'verbose':-1,
         }


np.random.seed(SEED)

loader = utils_cat.LoadFiles(['../feature/train_'])


# =============================================================================
# load
# =============================================================================
X_train = loader.train()
y_train = utils.read_pickles('../data/label').values

if X_train.columns.duplicated().sum()>0:
    raise Exception(f'duplicated!: { X_train.columns[X_train.columns.duplicated()] }')
print('no dup :) ')
print(f'X_train.shape {X_train.shape}')

gc.collect()

CAT = list( set(X_train.columns) & set(loader.category()) )
print(f'CAT: {CAT}')

COL = X_train.columns.tolist()

# =============================================================================
# cv
# =============================================================================
dtrain = lgb.Dataset(X_train, y_train, categorical_feature=CAT )
gc.collect()

ret = lgb.cv(param, dtrain, 9999, nfold=NFOLD,
             early_stopping_rounds=100, verbose_eval=50,
             seed=SEED)

result = f"CV auc-mean({NFOLD}): {ret['multi_logloss-mean'][-1]} + {ret['multi_logloss-stdv'][-1]}"
print(result)

utils.send_line(result)


# =============================================================================
# train
# =============================================================================

model_all = []
nround_mean = 0
wloss_list = []
for i in range(LOOP):
    gc.collect()
    param['seed'] = np.random.randint(9999)
    ret, models = lgb.cv(param, dtrain, 9999, nfold=NFOLD,
                         early_stopping_rounds=100, verbose_eval=50,
                         seed=SEED)
    y_pred = ex.eval_oob(X_train, y_train, models, SEED, stratified=True, shuffle=True)
    wloss_list.append( log_loss(y_train, y_pred, labels = list(range(14))) )
    model_all += models
    nround_mean += len(ret['multi_logloss-mean'])
    gc.collect()

nround_mean = int((nround_mean/LOOP) * 1.3)

result = f"CV wloss: {np.mean(wloss_list)} + {np.std(wloss_list)}"
print(result)

utils.send_line(result)

imp = ex.getImp(model_all)
imp['split'] /= imp['split'].max()
imp['gain'] /= imp['gain'].max()
imp['total'] = imp['split'] + imp['gain']

imp.sort_values('total', ascending=False, inplace=True)
imp.reset_index(drop=True, inplace=True)


imp.to_csv(f'LOG/imp_{__file__}.csv', index=False)


# =============================================================================
# test
# =============================================================================

dtest = utils.read_pickles('../data/test_old')

gc.collect()

sub = pd.read_pickle('../data/sub.p')

y_pred = pd.Series(0, index=sub.index)

for model in tqdm(model_all):
    y_pred += pd.Series(model.predict(dtest[COL])).rank()
y_pred /= y_pred.max()
y_pred /= LOOP

sub['target'] = y_pred.values

sub.to_csv(SUBMIT_FILE_PATH, index=False, compression='gzip')

# =============================================================================
# submission
# =============================================================================
if EXE_SUBMIT:
    print('submit')
    utils.submit(SUBMIT_FILE_PATH, COMMENT)


#==============================================================================
utils.end(__file__)
#utils.stop_instance()
