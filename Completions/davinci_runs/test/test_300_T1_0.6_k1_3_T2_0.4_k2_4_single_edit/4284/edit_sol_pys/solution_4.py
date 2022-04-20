

#-------------------------------------------------------------------------------
# Name:        file
# Purpose:
#
# Author:      v.osipov & a.komarov
#
# Created:     16/10/2018
# Copyright:   (c) v.osipov 2018, a.komarov 2018
# Licence:     <your licence>
import os
import sys
import re


def get_file_content(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return file.read()
    else:
        print('File not found')
        sys.exit(1)


def get_file_lines(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return file.readlines()
    else:
        print('File not found')
        sys.exit(1)


def get_file_lines_count(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return len(file.readlines())
    else:
        print('File not found')
        sys.exit(1)


def get_file_words(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return re.findall(r'\w+', file.read())
    else:
        print('File not found')
        sys.exit(1)


def get_file_words_count(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return len(re.findall(r'\w+', file.read()))
    else:
        print('File not found')
        sys.exit(1)


def get_file_chars(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return re.findall(r'\w', file.read())
    else:
        print('File not found')
        sys.exit(1)


def get_file_chars_count(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return len(re.findall(r'\w', file.read()))
    else:
        print('File not found')
        sys.exit(1)


def get_file_stats(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return {'lines': len(file.readlines()),
                    'words': len(re.findall(r'\w+', file.read())),
                    'chars': len(re.findall(r'\w', file.read()))}
    else:
        print('File not found')
        sys.exit(1)


#-------------------------------------------------------------------------------

def main():
    print(get_file_content('file.py'))
    print(get_file_lines('file.py'))
    print(get_file_lines_count('file.py'))
    print(get_file_words('file.py'))
    print(get_file_words_count('file.py'))
    print(get_file_chars('file.py'))
    print(get_file_chars_count('file.py'))
    print(get_file_stats('file.py'))


if __name__ == '__main__':
    main()
