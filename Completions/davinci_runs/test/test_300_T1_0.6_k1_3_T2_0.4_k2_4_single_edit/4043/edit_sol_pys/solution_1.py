#!/usr/bin/python3

import os

def main():
    f = open('lines.txt')
    for line in f:
        print(line, end='')
    f.close()

if __name__ == "__main__": main()
