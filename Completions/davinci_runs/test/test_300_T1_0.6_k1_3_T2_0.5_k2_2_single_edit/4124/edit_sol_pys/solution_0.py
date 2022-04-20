import os
import re

def get_files(path):
    file_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list

def get_files_with_extension(path, extension):
    file_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(extension):
                file_list.append(os.path.join(root, file))
    return file_list

def get_files_with_pattern(path, pattern):
    file_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if re.match(pattern, file):
                file_list.append(os.path.join(root, file))
    return file_list

def get_files_with_extension_and_pattern(path, extension, pattern):
    file_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(extension) and re.match(pattern, file):
                file_list.append(os.path.join(root, file))
    return file_list
