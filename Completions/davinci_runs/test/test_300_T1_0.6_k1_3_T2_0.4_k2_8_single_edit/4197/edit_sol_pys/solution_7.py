#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 17:39:57 2018

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

import utils
utils.start(__file__)
#==============================================================================

SUBMIT_FILE_PATH = '../output/1201-1.csv.gz'

COMMENT = 'top1000 features'

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

# =============================================================================
# load
# =============================================================================

files_tr = sorted(glob('../data/train_f*.f'))
[print(i,f) for i,f in enumerate(files_tr)]

X = pd.concat([
                pd.read_feather(f) for f in tqdm(files_tr, mininterval=60)
               ], axis=1)
y = utils.load_target().target

X.drop(DROP, axis=1, inplace=True)

target_dict = {}
target_dict_r = {}
for i,e in enumerate(y.sort_values().unique()):
    target_dict[e] = i
    target_dict_r[i] = e

y = y.replace(target_dict)

if X.columns.duplicated().sum()>0:
    raise Exception(f'duplicated!: { X.columns[X.columns.duplicated()] }')
print('no dup :) ')
print(f'X.shape {X.shape}')

gc.collect()

COL = X.columns.tolist()

# =============================================================================
# cv
# =============================================================================
dtrain = lgb.Dataset(X, y, #categorical_feature=CAT, 
                     free_raw_data=False)
gc.collect()

model_all = []
nround_mean = 0
wloss_list = []
y_preds = []
for i in range(2):
    gc.collect()
    param['seed'] = np.random.randint(9999)
    ret, models = lgb.cv(param, dtrain, 99999, nfold=NFOLD, 
                         feval=utils.lgb_multi_weighted_logloss,
                         early_stopping_rounds=100, verbose_eval=50,
                         seed=SEED)
    y_pred = ex.eval_oob(X, y, models, SEED, stratified=True, shuffle=True, 
                         n_class=14)
    y_preds.append(y_pred)
    model_all += models
    nround_mean += len(ret['multi_logloss-mean'])
    wloss_list.append( ret['wloss-mean'][-1] )

nround_mean = int((nround_mean/2) * 1.3)

result = f"CV wloss: {np.mean(wloss_list)} + {np.std(wloss_list)}"
utils.send_line(result)

y_pred = np.mean(y_preds, axis=0)


imp = ex.getImp(model_all)
imp['split'] /= imp['split'].max()
imp['gain'] /= imp['gain'].max()
imp['total'] = imp['split'] + imp['gain']
imp.sort_values('total', ascending=False, inplace=True)
imp.reset_index(drop=True, inplace=True)


imp.to_csv(f'LOG/imp_{__file__}.csv', index=False)

"""

imp = pd.read_csv('LOG/imp_0915-1.py.csv')

"""

COL = imp.head(1000).feature.tolist()


# =============================================================================
# train
# =============================================================================

dtrain = lgb.Dataset(X[COL], y, #categorical_feature=CAT, 
                     free_raw_data=False)
gc.collect()

model_all = []
nround_mean = 0
wloss_list = []
y_preds = []
for i in range(LOOP):
    gc.collect()
    param['seed'] = np.random.randint(9999)
    ret, models = lgb.cv(param, dtrain, 99999, nfold=NFOLD, 
                         feval=utils.lgb_multi_weighted_logloss,
                         early_stopping_rounds=100, verbose_eval=50,
                         seed=SEED)
    y_pred = ex.eval_oob(X[COL], y, models, SEED, stratified=True, shuffle=True, 
                         n_class=14)
    y_preds.append(y_pred)
    model_all += models
    nround_mean += len(ret['multi_logloss-mean'])
    wloss_list.append( ret['wloss-mean'][-1] )

nround_mean = int((nround_mean/LOOP) * 1.3)

result = f"CV wloss: {np.mean(wloss_list)} + {np.std(wloss_list)}"
utils.send_line(result)

y_pred = np.mean(y_preds, axis=0)

# =============================================================================
# test
# =============================================================================

files_te = sorted(glob('../data/test_f*.f'))

X_test = pd.concat([
                pd.read_feather(f) for f in tqdm(files_te, mininterval=60)
               ], axis=1)

X_test.drop(DROP, axis=1, inplace=True)

for i,model in enumerate(tqdm(model_all)):
    y_pred += model.predict(X_test[COL])
y_pred /= len(model_all)

sub = pd.read_csv('../input/sample_submission.csv.zip')
df = pd.

n = int(input())
a = list(map(int, input().split()))

l = [0] * n

for i in range(n):
    l[a[i]-1] = i+1

for i in l:
    print(i)
