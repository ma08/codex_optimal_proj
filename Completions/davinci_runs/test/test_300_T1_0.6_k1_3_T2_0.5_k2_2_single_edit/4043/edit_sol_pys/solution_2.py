import os


def get_file_list(path):
    # return all file names in a folder
    # return a list of file names
    return os.listdir(path)


def get_file_name(file_path):
    # return file name from file path
    # return a string
    return os.path.basename(file_path)


def get_file_path(file_name):
    # return file path from file name
    # return a string
    return os.path.abspath(file_name)


def get_file_extension(file_name):
    # return file extension from file name
    # return a string
    return file_name.split(".")[-1]


def get_file_size(file_name):
    # return file size from file name
    # return an int
    return os.path.getsize(file_name)


def get_file_creation_time(file_name):
    # return file creation time from file name
    # return a datetime
    return os.path.getctime(file_name)


def get_file_modification_time(file_name):
    # return file modification time from file name
    # return a datetime
    return os.path.getmtime(file_name)


def get_file_access_time(file_name):
    # return file access time from file name
    # return a datetime
    return os.path.getatime(file_name)
