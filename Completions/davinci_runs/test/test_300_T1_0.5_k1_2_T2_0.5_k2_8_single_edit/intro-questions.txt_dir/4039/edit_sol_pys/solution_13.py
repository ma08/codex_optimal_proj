
import os
import sys
import time


def get_dir_info(dir_path):
    files = []
    dirs = []
    for file in os.listdir(dir_path):
        file_path = os.path.join(dir_path, file)
        if os.path.isfile(file_path):
            files.append(file)
        else:
            dirs.append(file)
    return files, dirs


def get_file_info(file_path):
    stat = os.stat(file_path)
    file_size = stat.st_size
    file_mode = stat.st_mode
    file_mtime = stat.st_mtime
    file_ctime = stat.st_ctime
    file_atime = stat.st_atime
    return file_size, file_mode, file_mtime, file_ctime, file_atime


def get_file_size(file_path):
    return get_file_info(file_path)[0]


def get_file_mode(file_path):
    return get_file_info(file_path)[1]


def get_file_mtime(file_path):
    return get_file_info(file_path)[2]


def get_file_ctime(file_path):
    return get_file_info(file_path)[3]


def get_file_atime(file_path):
    return get_file_info(file_path)[4]


def get_file_age(file_path):
    return time.time() - get_file_atime(file_path)


def get_file_content(file_path):
    with open(file_path, 'r') as f:
        return f.read()


def get_file_lines(file_path):
    with open(file_path, 'r') as f:
        return f.readlines()


def get_file_line_count(file_path):
    return len(get_file_lines(file_path))


def get_file_extension(file_path):
    return os.path.splitext(file_path)[1]


def get_file_name(file_path):
    return os.path.splitext(os.path.basename(file_path))[0]


def get_file_path(file_path):
    return os.path.dirname(file_path)


def get_file_type(file_path):
    return os.path.splitext(file_path)[1]


def get_file_types(file_paths):
    return [get_file_type(file_path) for file_path in file_paths]


def is_file_type(file_path, file_type):
    return get_file_type(file_path) == file_type


def is_file_type_in(file_path, file_types):
    return get_file_type(file_path) in file_types


def get_file_paths(dir_path, file_type=None):
    if file_type is None:
        return [os.path.join(dir_path, file) for file in os.listdir(dir_path)]
    else:
        file_paths = []
        for file in os.listdir(dir_path):
            file_path = os.path.join(dir_path, file)
            if is_file_type(file_path, file_type):
                file_paths.append(file_path)
        return file_paths


def get_file_paths_recursive(dir_path, file_type=None):
    file_paths = []
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            file_path = os.path.join(root, file)
            if file_type is None or is_file_type(file_path, file_type):
                file_paths.append(file_path)
    return file_paths


def get_file_paths_by_name(dir_path, file_name, file_type=None):
    file_paths = []
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            file_path = os.path.join(root, file)
            if file == file_name and (file_type is None or is_file_type(file_path, file_type)):
                file_paths.append(file_path)
    return file_paths


def get_file_paths_by_name_and_extension(dir_path, file_name, file_extension=None):
    file_paths = []
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if file == file_name:
                file_path = os.path.join(root, file)
                if file_extension is None or is_file_type(file_path, file_extension):
                    file_paths.append(file_path)
    return file_paths


def get_file_paths_by_extension(dir_path, file_extension):
    file_paths = []
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            file_path = os.path.join(root, file)
            if is_file_type(file_path, file_extension):
                file_paths.append(file_path)
    return file_paths


def get_file_paths_by_name_and_extensions(dir_path, file_name, file_extensions):
    file_paths = []
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if file == file_name:
                file_path = os.path.join(root, file)
                if is_file_type_in(file_path, file_extensions):
                    file_paths.append(file_path)
    return file_paths


def get_file_paths_by_extensions(dir_path, file_extensions):
    file_paths = []
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            file_path = os.path.join(root, file)
            if is_file_type_in(file_path, file_extensions):
                file_paths.append(file_path)
    return file_paths


def get_file_paths_by_age(dir_path, file_type=None, age_threshold=0):
    file_paths = []
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            file_path = os.path.join(root, file)
            if get_file_age(file_path) >= age_threshold and (file_type is None or is_file_type(file_path, file_type)):
                file_paths.append(file_path)
    return file_paths


def get_file_paths_by_size(dir_path, file_type=None, size_threshold=0):
    file_paths = []
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            file_path = os.path.join(root, file)
            if get_file_size

def main():
    pass

if __name__ == "__main__":
    main()
