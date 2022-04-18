import os
import sys
import json

def file_list(path):
    dir_list = os.listdir(path)
    if not dir_list:
        return
    else:
        for file in dir_list:
            file_path = os.path.join(path, file)
            if os.path.isdir(file_path):
                file_list(file_path)
            elif os.path.isfile(file_path):
                print(file_path)

def main():
    file_list(sys.argv[1])

if __name__ == '__main__':
    main()
