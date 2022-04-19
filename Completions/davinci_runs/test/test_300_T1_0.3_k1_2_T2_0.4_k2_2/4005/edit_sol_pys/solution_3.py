
import os
import sys
import argparse
import re


def get_args():
    parser = argparse.ArgumentParser(description='File')
    parser.add_argument('-f', '--file', help='File name', required=True)
    parser.add_argument('-p', '--path', help='Path to file', required=True)
    parser.add_argument('-t', '--type', help='File type', required=True)
    parser.add_argument('-c', '--content', help='File content', required=True)
    args = parser.parse_args()
    return args


def create_file(file, path, type, content):
    if not os.path.exists(path):
        os.makedirs(path)
    f = open(path + '/' + file + '.' + type, 'w+')
    f.write(content)
    f.close()


def main():
    args = get_args()
    create_file(args.file, args.path, args.type, args.content)


if __name__ == '__main__':
    main()
