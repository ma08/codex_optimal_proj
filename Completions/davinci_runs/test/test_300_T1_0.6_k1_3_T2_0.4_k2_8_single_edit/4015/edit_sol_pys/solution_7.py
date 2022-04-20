#!/usr/bin/env python3

import sys

def main():
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
        print(file_name)
    else:
        print("No file name")

if __name__ == '__main__':
    main()
