import os
import os.path
import shutil
import sys
import time


def walk_dir(dir,topdown=True):
    for root, dirs, files in os.walk(dir,topdown):
        for name in files:
            print(os.path.join(root,name))
        for name in dirs:
            print(os.path.join(root,name))

def get_file_size(file):
    return os.path.getsize(file)

def get_file_modify_time(file):
    return time.strftime("%Y-%m-%d %H:%M:%S",time.gmtime(os.path.getmtime(file)))

def copy_file(src,dst):
    shutil.copy(src,dst)

def move_file(src,dst):
    shutil.move(src,dst)

def remove_file(file):
    os.remove(file)

def remove_dir(dir):
    shutil.rmtree(dir)

def main():
    print("hello,world")

if __name__ == '__main__':
    main()
