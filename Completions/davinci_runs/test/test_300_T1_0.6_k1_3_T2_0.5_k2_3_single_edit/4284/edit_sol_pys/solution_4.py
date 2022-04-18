

import os
import sys
import time
import shutil
import datetime
import configparser
def get_dir():
    return os.getcwd()

def get_file(dir):
    file_name = input('Введите имя файла:')
    return os.path.join(dir,file_name)

def get_file_list(dir):
    return os.listdir(dir)

def get_file_info(file):
    return os.stat(file)

def get_file_size(file):
    return os.path.getsize(file)

def get_file_date(file):
    return time.ctime(os.path.getmtime(file))

def get_file_name(file):
    return os.path.basename(file)

def get_file_ext(file):
    return os.path.splitext(file)

def get_file_mode(file):
    return os.path.isfile(file)

def copy_file(file,dir):
    return shutil.copy(file,dir)

def move_file(file,dir):
    return shutil.move(file,dir)

def del_file(file):
    return os.remove(file)

def create_file(file):
    return open(file, 'w')

def create_dir(dir):
    return os.mkdir(dir)

def del_dir(dir):
    return os.rmdir(dir)

def get_dir_list(dir):
    return os.listdir(dir)

def get_file_list(dir):
    return os.listdir(dir)

def get_dir_info(dir):
    return os.stat(dir)

def get_dir_size(dir):
    return os.path.getsize(dir)

def get_dir_date(dir):
    return time.ctime(os.path.getmtime(dir))

def get_dir_name(dir):
    return os.path.basename(dir)

def get_dir_mode(dir):
    return os.path.isdir(dir)

def get_dir_parent(dir):
    return os.path.dirname(dir)

def get_dir_root(dir):
    return os.path.abspath(dir)

def get_dir_tree(dir):
    return os.walk(dir)

def get_file_str(file):
    return open(file).read()

def get_file_line(file):
    return open(file).readline()

def get_file_lines(file):
    return open(file).readlines()

def get_file_csv(file):
    return csv.reader(open(file))

def get_file_ini(file):
    return configparser.ConfigParser()

def get_file_json(file):
    return json.load(open(file))

def get_file_xml(file):
    return minidom.parse(file)

def get_file_yaml(file):
    return yaml.load(open(file))

def get_file_xml(file):
    return minidom.parse(file)

def get_file_yaml(file):
    return yaml.load(open(file))

def get_file_csv(file):
    return csv.reader(open(file))

def get_file_ini(file):
    return configparser.ConfigParser()

def get_file_json(file):
    return json.load(open(file))

def get_file_xml(file):
    return minidom.parse(file)

def get_file_yaml(file):
    return yaml.load(open(file))

def move_file(file,dir):
    return shutil.move(file,dir)

def del_file(file):
    return os.remove(file)

def create_file(file):
    return open(file, 'w')

def create_dir(dir):
    return os.mkdir(dir)

def del_dir(dir):
    return os.rmdir(dir)

def get_dir_list(dir):
    return os.listdir(dir)

def get_file_list(dir):
    return os.listdir(dir)

def get_dir_info(dir):
    return os.stat(dir)

def get_dir_size(dir):
    return os.path.getsize(dir)

def get_dir_date(dir):
    return time.ctime(os.path.getmtime(dir))

def get_dir_name(dir):
    return os.path.basename(dir)

def get_dir_mode(dir):
    return os.path.isdir(dir)

def get_dir_parent(dir):
    return os.path.dirname(dir)

def get_dir_root(dir):
    return os.path.abspath(dir)

def get_dir_tree(dir):
    return os.walk(dir)

def get_file_str(file):
    return open(file).read()

def get_file_line(file):
    return open(file).readline()

def get_file_lines(file):
    return open(file).readlines()

def get_file_csv(file):
    return csv.reader(open(file))

def get_file_ini(file):
    return configparser.ConfigParser()

def get_file_json(file):
    return json.load(open(file))

def get_file_xml(file):
    return minidom.parse(file)

def get_file_yaml(file):
    return yaml.load(open(file))

def get_file_xml(file):
    return minidom.parse(file)

def get_file_yaml(file):
    return yaml.load(open(file))

def get_file_csv(file):
    return csv.reader(open(file))

def get_file_ini(file):
    return configparser.ConfigParser()

def get_file_json(file):
    return json.load(open(file))

def get_file_xml(file):
    return minidom.parse(file)

def get_file_yaml(file):
    return yaml.load(open(file))
import csv

def main():
    print('Hello')
    dir = get_dir()
    print(dir)
    file = get_file(dir)
    print(file)
    print(get_file_list(dir))
    print(get_file_info(file))
    print(get_file_size(file))
    print(get_file_date(file))
    print(get_file_name(file))
    print(get_file_ext(file))
    print(get_file_mode

if __name__ == '__main__':
    main()
