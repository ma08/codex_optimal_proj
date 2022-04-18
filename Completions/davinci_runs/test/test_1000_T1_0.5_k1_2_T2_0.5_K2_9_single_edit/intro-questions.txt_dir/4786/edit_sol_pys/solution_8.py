#!/usr/bin/env python3

import sys
import math

def main():
    n = int(sys.stdin.readline().strip())
    keywords = []
    for i in range(n):
        keyword = sys.stdin.readline().strip().lower().replace("-", " ")
        if keyword not in keywords:
            keywords.append(keyword)
    print(len(keywords)) # print the number of keywords

if __name__ == "__main__": # if the script is called from the command line
    main()
