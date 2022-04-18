import os
import sys
import json


def get_config():
    with open('config.json') as f:
        config = json.load(f)
    return config


def get_path(config):
    return config['path']


def get_files(path):
    return os.listdir(path)


def get_extension(file):
    return os.path.splitext(file)[1]


def get_extensions(files):
    return [get_extension(file) for file in files]


def get_unique_extensions(extensions):
    return set(extensions)


def create_folders(path, extensions):
    for extension in extensions:
        folder_name = extension[1:]
        os.mkdir(os.path.join(path, folder_name))


def move_files(path, files, extensions):
    for file in files:
        extension = get_extension(file)
        folder_name = extension[1:]
        os.rename(os.path.join(path, file),
                  os.path.join(path, folder_name, file))


def main():
    config = get_config()
    path = get_path(config)
    files = get_files(path)
    extensions = get_extensions(files)
    unique_extensions = get_unique_extensions(extensions)
    create_folders(path, unique_extensions)
    move_files(path, files, unique_extensions)


if __name__ == '__main__':
    main()
