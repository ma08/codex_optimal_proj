#!/usr/bin/python3

import sys
import os
import argparse

def main():
    parser = argparse.ArgumentParser(description='File manipulation')
    parser.add_argument('-c', '--create', help='Create file')
    parser.add_argument('-r', '--read', help='Read file')
    parser.add_argument('-u', '--update', help='Update file')
    parser.add_argument('-d', '--delete', help='Delete file')
    parser.add_argument('-s', '--search', help='Search for a word')
    parser.add_argument('-a', '--append', help='Append to file')
    args = parser.parse_args()

    if args.create:
        create(args.create)
    elif args.read:
        read(args.read)
    elif args.update:
        update(args.update)
    elif args.delete:
        delete(args.delete)
    elif args.search:
        search(args.search)
    elif args.append:
        append(args.append)
    else:
        print("Error: No input provided")

def create(file_name):
    if os.path.exists(file_name):
        print("Error: File already exists")
    else:
        f = open(file_name, 'w+')
        f.close()

def read(file_name):
    if os.path.exists(file_name):
        f = open(file_name, 'r')
        print(f.read())
        f.close()
    else:
        print("Error: File does not exist")

def update(file_name):
    if os.path.exists(file_name):
        f = open(file_name, 'w')
        f.write(input("Enter a string to write to the file: "))
        f.close()
    else:
        print("Error: File does not exist")

def delete(file_name):
    if os.path.exists(file_name):
        os.remove(file_name)
    else:
        print("Error: File does not exist")

def search(file_name):
    if os.path.exists(file_name):
        f = open(file_name, 'r')
        if args.search in f.read():
            print("Word is in file")
        else:
            print("Word is not in file")
        f.close()
    else:
        print("Error: File does not exist")

def append(file_name):
    if os.path.exists(file_name):
        f = open(file_name, 'a')
        f.write(input("Enter a string to append to the file: "))
        f.close()
    else:
        print("Error: File does not exist")

if __name__ == "__main__":
    main()
