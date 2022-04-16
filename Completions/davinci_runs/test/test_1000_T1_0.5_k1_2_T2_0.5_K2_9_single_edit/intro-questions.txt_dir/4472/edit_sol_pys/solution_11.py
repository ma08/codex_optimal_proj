#!/usr/bin/env python3

import os
import glob

def main():
    print("This is the files program.")
    print()

    # change to desired directory
    os.chdir("/home/student/mycode/")

    # print a list of all files in current directory
    print(glob.glob('*'))

    # create a new directory
    os.mkdir('/home/student/mycode/test')

    # move to new directory
    os.chdir('/home/student/mycode/test')

    # print a list of all files in current directory
    print(glob.glob('*'))

    # create a new file
    with open("file3.txt", "w") as f:
        f.write("This is file3.")

    # print a list of all files in current directory
    print(glob.glob('*'))

    # rename a file
    os.rename("file3.txt", "file4.txt")

    # print a list of all files in current directory
    print(glob.glob('*'))

    # move a file to a different directory
    os.rename("file4.txt", "/home/student/mycode/file4.txt")

    # print a list of all files in current directory
    print(glob.glob('*'))

    # change directories to the parent directory
    os.chdir("/home/student/mycode/")

    # remove the directory
    os.rmdir("/home/student/mycode/test")

    # print a list of all files in current directory
    print(glob.glob('*'))

    # delete a file
    os.remove("file4.txt")

    # print a list of all files in current directory
    print(glob.glob('*'))

    # delete a directory
    os.rmdir("/home/student/mycode/test")

if __name__ == "__main__":
    main()
