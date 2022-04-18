#!/usr/bin/env python


import os
import re

def main():
    path = os.getcwd()
    files = os.listdir(path)
    for f in files:
        if re.match(r'^\d{3}-\d{4}-\d{4}$', f):
            print(f)



if __name__ == '__main__':
    main()
