#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys

def main():
    # get the current directory and print it
    currentDirectory = os.getcwd()
    print(currentDirectory)

    # change the directory
    os.chdir("/home/jie/Documents/GitHub/Python")

    # get the current directory and print it
    currentDirectory = os.getcwd()
    print(currentDirectory)

    # get the directory list and print it
    directoryList = os.listdir(currentDirectory)
    print(directoryList)

    # create a new directory
    os.mkdir("newDirectory")

    # get the directory list and print it
    directoryList = os.listdir(currentDirectory)
    print(directoryList)

    # remove the directory
    os.rmdir("newDirectory")

    # get the directory list and print it
    directoryList = os.listdir(currentDirectory)
    print(directoryList)

    # create a new file
    file1 = open("test.txt", "w")
    file1.write("Hello World!")
    file1.close()

    # remove the file
    os.remove("test.txt")

    # get the directory list and print it
    directoryList = os.listdir(currentDirectory)
    print(directoryList)

if __name__ == '__main__':
    main()
