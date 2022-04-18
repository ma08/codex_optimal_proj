import os
import shutil
import sys


def main():
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        path = input("Enter the path to the directory: ")
    print("Path: " + path)
    for file in os.listdir(path):
        if os.path.isdir(os.path.join(path, file)):
            print("Directory: " + file)
        else:
            print("File: " + file)


if __name__ == '__main__':
    main()
