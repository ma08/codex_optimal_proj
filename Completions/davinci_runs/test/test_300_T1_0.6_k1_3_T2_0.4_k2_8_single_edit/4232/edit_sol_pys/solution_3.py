#!/usr/bin/python3


import os
from os import path

def main():
    print(os.name)

    print("Item exists: " + str(path.exists("textfile.txt")))
    print("Item is a file: " + str(path.isfile("textfile.txt")))
    print("Item is a directory: " + str(path.isdir("textfile.txt")))

    print("Item's path: " + str(path.realpath("textfile.txt")))
    print("Item's path and name: " + str(path.split(path.realpath("textfile.txt"))))

    t = path.getmtime("textfile.txt")
    print(t)

    from datetime import datetime
    print(datetime.fromtimestamp(t))

    print(path.splitext("textfile.txt"))

if __name__ == "__main__":
    main()
