#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 15:58:50 2018

@author: hu
"""

import os
import glob

def get_file_path(root_path, file_name, file_type=''):
    '''
    get the file path
    root_path: root path of the dataset
    file_name: name of the file
    file_type: type of the file
    '''
    return os.path.join(root_path, file_name, file_type)

def get_file_list(file_path):
    '''
    get the file list
    file_path: path of the file
    '''
    return glob.glob(file_path)




