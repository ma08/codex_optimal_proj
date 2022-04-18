

import os
import sys
import re
import json


def get_files_in_directory(path):
    """
    get all files in directory
    """
    files = []
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            files.append(file)
    return files


def get_json_files(files):
    """
    get json files from files
    """
    json_files = []
    for file in files:
        if file.endswith('.json'):
            json_files.append(file)
    return json_files


def get_json_file_name(json_file):
    """
    get json file name
    """
    json_file_name = json_file.replace('.json', '')
    return json_file_name


def get_json_file_content(json_file):
    """
    get json file content
    """
    with open(json_file, 'r') as f:
        content = f.read()
    return content


def get_json_file_content_list(json_file_content):
    """
    get json file content list
    """
    json_file_content_list = json.loads(json_file_content)
    return json_file_content_list


def get_json_file_content_list_length(json_file_content_list):
    """
    get json file content list length
    """
    json_file_content_list_length = len(json_file_content_list)
    return json_file_content_list_length


def get_json_file_content_list_item(json_file_content_list, index):
    """
    get json file content list item
    """
    json_file_content_list_item = json_file_content_list[index]
    return json_file_content_list_item


def get_json_file_content_list_item_keys(json_file_content_list_item):
    """
    get json file content list item keys
    """
    json_file_content_list_item_keys = json_file_content_list_item.keys()
    return json_file_content_list_item_keys


def get_json_file_content_list_item_values(json_file_content_list_item):
    """
    get json file content list item values
    """
    json_file_content_list_item_values = json_file_content_list_item.values()
    return json_file_content_list_item_values


def get_json_file_content_list_item_value(json_file_content_list_item_values, index):
    """
    get json file content list item value
    """
    json_file_content_list_item_value = json_file_content_list_item_values[index]
    return json_file_content_list_item_value


def get_json_file_content_list_item_value_keys(json_file_content_list_item_value):
    """
    get json file content list item value keys
    """
    json_file_content_list_item_value_keys = json_file_content_list_item_value.keys()
    return json_file_content_list_item_value_keys


def get_json_file_content_list_item_value_values(json_file_content_list_item_value):
    """
    get json file content list item value values
    """
    json_file_content_list_item_value_values = json_file_content_list_item_value.values()
    return json_file_content_list_item_value_values


def get_json_file_content_list_item_value_value(json_file_content_list_item_value_values, index):
    """
    get json file content list item value value
    """
    json_file_content_list_item_value_value = json_file_content_list_item_value_values[index]
    return json_file_content_list_item_value_value


def get_json_file_content_list_item_value_value_keys(json_file_content_list_item_value_value):
    """
    get json file content list item value value keys
    """
    json_file_content_list_item_value_value_keys = json_file_content_list_item_value_value.keys()
    return json_file_content_list_item_value_value_keys


def get_json_file_content_list_item_value_value_values(json_file_content_list_item_value_value):
    """
    get json file content list item value value values
    """
    json_file_content_list_item_value_value_values = json_file_content_list_item_value_value.values()
    return json_file_content_list_item_value_value_values


def get_json_file_content_list_item_value_value_value(json_file_content_list_item_value_value_values, index):
    """
    get json file content list item value value value
    """
    json_file_content_list_item_value_value_value = json_file_content_list_item_value_value_values[index]
    return json_file_content_list_item_value_value_value


def get_json_file_content_list_item_value_value_value_keys(json_file_content_list_item_value_value_value):
    """
    get json file content list item value value value keys
    """
    json_file_content_list_item_value_value_value_keys = json_file_content_list_item_value_value_value.keys()
    return json_file_content_list_item_value_value_value_keys


def get_json_file_content_list_item_value_value_value_values(json_file_content_list_item_value_value_value):
    """
    get json file content list item value value value values
    """
    json_file_content_list_item_value_value_value_values = json_file_content_list_item_value_value_value.values()
    return json_file_content_list_item_value_value_value_values


def get_json_file_content_list_item_value_value_value_value(json_file_content_list_item_value_value_value_values, index):
    """
    get json file content list item value value value value
    """
    json_file_content_list_item_value_value_value_value = json_file_content_list_item_value_value_value_values[index]
    return json_file_content_list_item_value_value_value_value


def get_json_file_content_list_item_value_value_value_value_keys(json_file_content_list_item_value_value_value_value):
    """
    get json file content list item value value value value keys
    """
    json_file_content_list_item_value_value_value
