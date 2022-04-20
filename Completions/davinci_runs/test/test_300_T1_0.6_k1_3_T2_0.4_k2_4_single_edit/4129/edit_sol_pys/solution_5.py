#!/usr/bin/python

import sys
import re


def main():
    if len(sys.argv) <= 1:
        print("Usage: file.py <file>")
        return

    file = open(sys.argv[1], "r")
    text = file.read()
    file.close()

    # print(text)

    # text = re.sub(r'\s+', ' ', text)
    # print(text)

    text = re.sub(r'\n', '', text)
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'\s+\.', '.', text)
    text = re.sub(r'\s+\,', ',', text)
    text = re.sub(r'\s+\:', ':', text)
    text = re.sub(r'\s+\;', ';', text)
    text = re.sub(r'\s+\?', '?', text)
    text = re.sub(r'\s+\!', '!', text)

    print(text)


if __name__ == "__main__":
    main()
