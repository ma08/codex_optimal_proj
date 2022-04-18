#!/usr/bin/env python

import os

def file_search(folder, filename):
    for dirpath, dirnames, filenames in os.walk(folder):
        for name in filenames:
            if name == filename:
                return os.path.join(dirpath, name)

    return None


if __name__ == "__main__":
    folder = os.path.expanduser("~")
    filename = "test.txt"
    print(file_search(folder, filename))
