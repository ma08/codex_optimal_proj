
import argparse
import sys
import os
from os import path
from os import listdir
from os.path import isfile, join

def read_file(file_name):
    f = open(file_name, "r")
    content = f.read()
    f.close()
    return content

def write_file(file_name, content):
    f = open(file_name, "w")
    f.write(content)
    f.close()

def append_file(file_name, content):
    f = open(file_name, "a")
    f.write(content)
    f.close()

def list_files_in_folder(folder):
    files = [f for f in listdir(folder) if isfile(join(folder, f))]
    return files

def get_file_extension(file_name):
    return file_name.split(".")[-1]

def get_file_name(file_name):
    return file_name.split(".")[0]

def get_file_name_extension(file_name):
    return ".".join(file_name.split(".")[:-1])

def get_file_size(file_name):
    return path.getsize(file_name)

def get_file_content(file_name):
    return read_file(file_name)

def set_file_content(file_name, content):
    write_file(file_name, content)

def add_file_content(file_name, content):
    append_file(file_name, content)

def main():
    parser = argparse.ArgumentParser(description='File utility tool')
    parser.add_argument('-l', '--list', dest='list', action='store_true', help='list files in folder')
    parser.add_argument('-e', '--extension', dest='extension', action='store_true', help='get file extension')
    parser.add_argument('-n', '--name', dest='name', action='store_true', help='get file name')
    parser.add_argument('-ne', '--nameextension', dest='nameextension', action='store_true', help='get file name extension')
    parser.add_argument('-s', '--size', dest='size', action='store_true', help='get file size')
    parser.add_argument('-c', '--content', dest='content', action='store_true', help='get file content')
    parser.add_argument('-sc', '--setcontent', dest='setcontent', action='store_true', help='set file content')
    parser.add_argument('-ac', '--addcontent', dest='addcontent', action='store_true', help='add file content')
    parser.add_argument('--file', dest='file', action='store', help='file name')
    parser.add_argument('--folder', dest='folder', action='store', help='folder name')
    parser.add_argument('--content-file', dest='content_file', action='store', help='content file name')
    parser.add_argument('--content-value', dest='content_value', action='store', help='content value')

    args = parser.parse_args()

    if args.list:
        if args.folder:
            files = list_files_in_folder(args.folder)
            print(files)
        else:
            print("No folder specified")
    elif args.extension:
        if args.file:
            extension = get_file_extension(args.file)
            print(extension)
        else:
            print("No file specified")
    elif args.name:
        if args.file:
            name = get_file_name(args.file)
            print(name)
        else:
            print("No file specified")
    elif args.nameextension:
        if args.file:
            name_extension = get_file_name_extension(args.file)
            print(name_extension)
        else:
            print("No file specified")
    elif args.size:
        if args.file:
            size = get_file_size(args.file)
            print(size)
        else:
            print("No file specified")
    elif args.content:
        if args.file:
            content = get_file_content(args.file)
            print(content)
        else:
            print("No file specified")
    elif args.setcontent:
        if args.file and args.content_value:
            set_file_content(args.file, args.content_value)
        else:
            print("No file or content value specified")
    elif args.addcontent:
        if args.file and args.content_value:
            add_file_content(args.file, args.content_value)
        elif args.file and args.content_file:
            content = get_file_content(args.content_file)
            add_file_content(args.file, content)
        else:
            print("No file or content value/file specified")
    else:
        print("No action specified")

if __name__ == "__main__":
    main()
