#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 15:58:50 2018

@author: hu
"""

import os
import glob
import cv2

def get_file_path(root_path, file_name, file_type):
    '''
    get the file path
    root_path: root path of the dataset
    file_name: name of the file
    file_type: type of the file
    '''
    return os.path.join(root_path, file_name, '*' + file_type)

def get_file_list(file_path):
    '''
    get the file list
    file_path: path of the file
    '''
    return glob.glob(file_path)
def get_image(img_path):
    '''
    get the image
    img_path: path of the image
    '''
    return cv2.imread(img_path)

def get_image_list(img_path_list):
    '''
    get the image list
    img_path_list: list of image path
    '''
    return [cv2.imread(img_path) for img_path in img_path_list]

def get_image_list_by_file(root_path, file_name, file_type):
    '''
    get the image list by file
    root_path: root path of the dataset
    file_name: name of the file
    file_type: type of the file
    '''
    return get_image_list(get_file_list(get_file_path(root_path, file_name, file_type)))


