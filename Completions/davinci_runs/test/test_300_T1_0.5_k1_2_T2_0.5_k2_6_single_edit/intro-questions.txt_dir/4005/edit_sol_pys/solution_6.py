import os
import shutil
import time


def find_file(path):
    for root, dirs, files in os.walk(path):
        for name in files:
            if name == "file.py":
                print(os.path.join(root, name))


def find_file_with_ext(path, ext):
    for root, dirs, files in os.walk(path):
        for name in files:
            if name.endswith(ext):
                print(os.path.join(root, name))


def find_file_with_size(path, size):
    for root, dirs, files in os.walk(path):
        for name in files:
            if os.stat(os.path.join(root, name)).st_size > size:
                print(os.path.join(root, name))


def find_file_with_time(path, time_):
    for root, dirs, files in os.walk(path):
        for name in files:
            if os.stat(os.path.join(root, name)).st_mtime > time_:
                print(os.path.join(root, name))


def copy_file(path_in, path_out):
    try:
        shutil.copy(path_in, path_out)
        print("File copied")
    except IOError:
        print("Error")


def copy_file_with_ext(path_in, path_out, ext):
    try:
        for root, dirs, files in os.walk(path_in):
            for name in files:
                if name.endswith(ext):
                    shutil.copy(os.path.join(root, name), path_out)
                    print("File copied")
    except IOError:
        print("Error")


def copy_file_with_size(path_in, path_out, size):
    try:
        for root, dirs, files in os.walk(path_in):
            for name in files:
                if os.stat(os.path.join(root, name)).st_size > size:
                    shutil.copy(os.path.join(root, name), path_out)
                    print("File copied")
    except IOError:
        print("Error")


def copy_file_with_time(path_in, path_out, time_):
    try:
        for root, dirs, files in os.walk(path_in):
            for name in files:
                if os.stat(os.path.join(root, name)).st_mtime > time_:
                    shutil.copy(os.path.join(root, name), path_out)
                    print("File copied")
    except IOError:
        print("Error")


def main():
    print("1. find file")
    print("2. find file with ext")
    print("3. find file with size")
    print("4. find file with time")
    print("5. copy file")
    print("6. copy file with ext")
    print("7. copy file with size")
    print("8. copy file with time")
    print("0. exit")
    while True:
        choice = int(input("choice: "))
        if choice == 1:
            find_file("/home/ilya/PycharmProjects/untitled")
        elif choice == 2:
            find_file_with_ext("/home/ilya/PycharmProjects/untitled", ".py")
        elif choice == 3:
            find_file_with_size("/home/ilya/PycharmProjects/untitled", 100)
        elif choice == 4:
            find_file_with_time("/home/ilya/PycharmProjects/untitled", time.time() - 60)
        elif choice == 5:
            copy_file("/home/ilya/PycharmProjects/untitled/file.py", "/home/ilya/PycharmProjects/untitled/file1.py")
        elif choice == 6:
            copy_file_with_ext("/home/ilya/PycharmProjects/untitled", "/home/ilya/PycharmProjects/untitled", ".py")
        elif choice == 7:
            copy_file_with_size("/home/ilya/PycharmProjects/untitled", "/home/ilya/PycharmProjects/untitled", 100)
        elif choice == 8:
            copy_file_with_time("/home/ilya/PycharmProjects/untitled", "/home/ilya/PycharmProjects/untitled", time.time() - 60)
        elif choice == 0:
            break
        else:
            print("Error")


if __name__ == '__main__':
    main()
