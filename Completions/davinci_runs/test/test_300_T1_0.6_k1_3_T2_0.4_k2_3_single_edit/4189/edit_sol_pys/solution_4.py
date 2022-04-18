import os


def get_file_list(path):
    file_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list


def get_file_ext(file_name):
    return os.path.splitext(file_name)[1]


def get_file_name(file_path):
    return os.path.splitext(os.path.basename(file_path))[0]
