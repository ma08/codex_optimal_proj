import os
import sys


def get_file_list(dir_path):
    file_list = []
    for path, dirs, files in os.walk(dir_path):
        for f in files:
            file_list.append(os.path.join(path, f))
    return file_list


def get_file_list_by_ext(dir_path, ext):
    file_list = []
    for path, dirs, files in os.walk(dir_path):
        for f in files:
            if f.endswith(ext):
                file_list.append(os.path.join(path, f))
    return file_list


def get_file_list_by_ext_list(dir_path, ext_list):
    file_list = []
    for path, dirs, files in os.walk(dir_path):
        for f in files:
            for ext in ext_list:
                if f.endswith(ext):
                    file_list.append(os.path.join(path, f))
                    break
    return file_list


def get_dir_list(dir_path):
    dir_list = []
    for path, dirs, files in os.walk(dir_path):
        for d in dirs:
            dir_list.append(os.path.join(path, d))
    return dir_list


def get_file_name(file_path):
    return os.path.basename(file_path)


def get_file_name_without_ext(file_path):
    return os.path.splitext(os.path.basename(file_path))[0]


def get_file_ext(file_path):
    return os.path.splitext(os.path.basename(file_path))[1]


def get_file_size(file_path):
    return os.path.getsize(file_path)


def get_file_size_in_mb(file_path):
    return os.path.getsize(file_path) / 1024 / 1024


def get_file_size_in_gb(file_path):
    return os.path.getsize(file_path) / 1024 / 1024 / 1024


def get_file_size_in_tb(file_path):
    return os.path.getsize(file_path) / 1024 / 1024 / 1024 / 1024


def get_file_size_in_format(file_path):
    return '{:.2f}'.format(os.path.getsize(file_path) / 1024 / 1024) + 'M'


def get_file_size_in_format_by_unit(file_path, unit):
    if unit == 'B':
        return '{:.2f}'.format(os.path.getsize(file_path)) + 'B'
    elif unit == 'K':
        return '{:.2f}'.format(os.path.getsize(file_path) / 1024) + 'K'
    elif unit == 'M':
        return '{:.2f}'.format(os.path.getsize(file_path) / 1024 / 1024) + 'M'
    elif unit == 'G':
        return '{:.2f}'.format(os.path.getsize(file_path) / 1024 / 1024 / 1024) + 'G'
    elif unit == 'T':
        return '{:.2f}'.format(os.path.getsize(file_path) / 1024 / 1024 / 1024 / 1024) + 'T'
    else:
        return '{:.2f}'.format(os.path.getsize(file_path)) + 'B'


def get_file_size_in_format_by_size(file_path, size):
    if size == 'B':
        return '{:.2f}'.format(os.path.getsize(file_path)) + 'B'
    elif size == 'K':
        return '{:.2f}'.format(os.path.getsize(file_path) / 1024) + 'K'
    elif size == 'M':
        return '{:.2f}'.format(os.path.getsize(file_path) / 1024 / 1024) + 'M'
    elif size == 'G':
        return '{:.2f}'.format(os.path.getsize(file_path) / 1024 / 1024 / 1024) + 'G'
    elif size == 'T':
        return '{:.2f}'.format(os.path.getsize(file_path) / 1024 / 1024 / 1024 / 1024) + 'T'
    else:
        return '{:.2f}'.format(os.path.getsize(file_path)) + 'B'


def get_file_create_time(file_path):
    return os.path.getctime(file_path)


def get_file_modify_time(file_path):
    return os.path.getmtime(file_path)


def get_file_access_time(file_path):
    return os.path.getatime(file_path)


def get_file_content(file_path):
    with open(file_path, 'r') as f:
        return f.read()


def get_file_content_by_line(file_path):
    with open(file_path, 'r') as f:
        return f.readlines()


def write_file_content(file_path, content):
    with open(file_path, 'w') as f:
        f.write(content)


def write_file_content_by_line(file_path, content_list):
    with open(file_path, 'w') as f:
        f.writelines(content_list)


def append_file_content(file_path, content):
    with open(file_path, 'a') as f:
        f.write(content)


def append_file_content_by_line(file_path, content_list):
    with open(file_path, 'a') as f:
        f.writelines(content_list)


def delete_file(file_path):
    os.remove(file_path)


def copy_file(file_path, new_file_path):
    with open(file_path, 'rb') as f:
        with open(new_file_path, 'wb') as f_new:
            f_new.write(f.read())


def move_file(file_path, new_file_path):
    os.rename(file_path, new_file_path)


def rename_file(file_path, new_file_path):
    os.rename(file_path, new_file_path)


def create_dir(dir_path):
    os.mkdir(dir_path)


def delete_dir(dir_path):
    os.rmdir(dir_path)


def copy_dir(dir_path, new_dir_path):
    os.system('xcopy ' + dir_path + ' ' + new_dir_path + ' /e /q /y')


def move_dir(dir_path, new_dir_path):
    os.rename(dir_path, new_dir_path)


def rename_dir(dir_path, new_dir_path):
    os.rename(dir_path, new_dir_path)
