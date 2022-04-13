#! /usr/bin/env python3

import sys

def main():
    n = int(sys.stdin.readline().strip())
    keywords = []
    for i in range(n):
        keyword = sys.stdin.readline().strip().lower().replace("-", " ")
        if keyword not in keywords:
            keywords.append(keyword)
    print(len(keywords))

if __name__ == "__main__":
    main()
