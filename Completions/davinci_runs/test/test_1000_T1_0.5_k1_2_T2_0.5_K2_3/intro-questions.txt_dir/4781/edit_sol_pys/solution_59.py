#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  1 09:55:07 2019


@author: lisun
"""

import pandas as pd

data_path = 'data/'


def get_data():
    train = pd.read_csv(data_path + 'train.csv')
    test = pd.read_csv(data_path + 'test.csv')
    return train, test

def main():
    train, test = get_data()
    print(train.shape, test.shape)

if __name__ == '__main__':
    main()
