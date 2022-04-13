

import os
import glob
import re


def get_full_path_of_files(path, file_name):
    files = glob.glob(os.path.join(path, file_name))
    return files


def get_file_names(path, file_name):
    files = glob.glob(os.path.join(path, file_name))
    files = [os.path.basename(x) for x in files]
    return files


def get_file_names_with_regex(path, regex):
    files = glob.glob(os.path.join(path, regex))
    files = [os.path.basename(x) for x in files]
    return files


def get_file_names_with_regex_and_conditions(path, regex, conditions):
    files = glob.glob(os.path.join(path, regex))
    files = [os.path.basename(x) for x in files]

    for condition in conditions:
        files = [x for x in files if condition in x]

    return files


if __name__ == "__main__":
    path = '/Users/jiajunluo/Dropbox/data'
    file_name = '*.csv'
    regex = '*.csv'
    conditions = ['AAPL', 'GOOG']

    print(get_full_path_of_files(path, file_name))
    print(get_file_names(path, file_name))
    print(get_file_names_with_regex(path, regex))
    print(get_file_names_with_regex_and_conditions(path, regex, conditions))
