import os
import pandas as pd
import numpy as np


def get_file_list(file_path, file_type):
    file_list = []
    if os.path.isdir(file_path):
        for file in os.listdir(file_path):
            if file.endswith(file_type):
                file_list.append(file)
    else:
        print('file path is not valid')
    return file_list


def get_data_frame(file_path, file_type):
    file_list = get_file_list(file_path, file_type)
    data_frame = pd.DataFrame()
    for file in file_list:
        data_frame_temp = pd.read_csv(file_path + file, header=None)
        data_frame = pd.concat([data_frame, data_frame_temp], axis=0)
    return data_frame


def get_data_frame_list(file_path, file_type):
    file_list = get_file_list(file_path, file_type)
    data_frame_list = []
    for file in file_list:
        data_frame_temp = pd.read_csv(file_path + file, header=None)
        data_frame_list.append(data_frame_temp)
    return data_frame_list


def get_data_frame_list_with_label(file_path, file_type):
    file_list = get_file_list(file_path, file_type)
    data_frame_list = []
    label = 0
    for file in file_list:
        data_frame_temp = pd.read_csv(file_path + file, header=None)
        data_frame_temp['label'] = label
        data_frame_list.append(data_frame_temp)
        label += 1
    return data_frame_list


def get_data_frame_list_with_label_and_index(file_path, file_type):
    file_list = get_file_list(file_path, file_type)
    data_frame_list = []
    label = 0
    for file in file_list:
        data_frame_temp = pd.read_csv(file_path + file, header=None)
        data_frame_temp['label'] = label
        data_frame_temp['index'] = data_frame_temp.index
        data_frame_list.append(data_frame_temp)
        label += 1
    return data_frame_list


def get_data_frame_list_with_label_and_index_and_time(file_path, file_type):
    file_list = get_file_list(file_path, file_type)
    data_frame_list = []
    label = 0
    for file in file_list:
        data_frame_temp = pd.read_csv(file_path + file, header=None)
        data_frame_temp['label'] = label
        data_frame_temp['index'] = data_frame_temp.index
        data_frame_temp['time'] = data_frame_temp.index * 0.02
        data_frame_list.append(data_frame_temp)
        label += 1
    return data_frame_list


def get_data_frame_list_with_label_and_index_and_time_and_file(file_path, file_type):
    file_list = get_file_list(file_path, file_type)
    data_frame_list = []
    label = 0
    for file in file_list:
        data_frame_temp = pd.read_csv(file_path + file, header=None)
        data_frame_temp['label'] = label
        data_frame_temp['index'] = data_frame_temp.index
        data_frame_temp['time'] = data_frame_temp.index * 0.02
        data_frame_temp['file'] = file
        data_frame_list.append(data_frame_temp)
        label += 1
    return data_frame_list


def get_data_frame_list_with_label_and_index_and_time_and_file_and_feature(file_path, file_type, feature_name):
    file_list = get_file_list(file_path, file_type)
    data_frame_list = []
    label = 0
    for file in file_list:
        data_frame_temp = pd.read_csv(file_path + file, header=None)
        data_frame_temp['label'] = label
        data_frame_temp['index'] = data_frame_temp.index
        data_frame_temp['time'] = data_frame_temp.index * 0.02
        data_frame_temp['file'] = file
        data_frame_temp['feature'] = feature_name
        data_frame_list.append(data_frame_temp)
        label += 1
    return data_frame_list


def get_data_frame_list_with_label_and_index_and_time_and_file_and_feature_and_feature_value(file_path, file_type, feature_name, feature_value):
    file_list = get_file_list(file_path, file_type)
    data_frame_list = []
    label = 0
    for file in file_list:
        data_frame_temp = pd.read_csv(file_path + file, header=None)
        data_frame_temp['label'] = label
        data_frame_temp['index'] = data_frame_temp.index
        data_frame_temp['time'] = data_frame_temp.index * 0.02
        data_frame_temp['file'] = file
        data_frame_temp['feature'] = feature_name
        data_frame_temp['feature_value'] = feature_value
        data_frame_list.append(data_frame_temp)
        label += 1
    return data_frame_list


def get_data_frame_list_with_label_and_index_and_time_and_file_and_feature_and_feature_value_and_feature_value_type(file_path, file_type, feature_name, feature_value, feature_value_type):
    file_list = get_file_list(file_path, file_type)
    data_frame_list = []
    label = 0
    for file in file_list:
        data_frame_temp = pd.read_csv(file_path + file, header=None)
        data_frame_temp['label'] = label
        data_frame_temp['index'] = data_frame_temp.index
        data_frame_temp['time'] = data_frame_temp.index * 0.02
        data_frame_temp['file'] = file
        data_frame_temp['feature'] = feature_name
        data_frame_temp['feature_value'] = feature_value
        data_frame_temp['feature_value_type'] = feature_value_type
        data_frame_list.append(data_frame_temp)
        label += 1
    return data_frame_list
