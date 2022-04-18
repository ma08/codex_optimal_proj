"""
File: file.py
Author: setcain
Email: setcain@gmail.com
Github: https://github.com/setcain
Description: This file is used to solve problem from https://www.hackerrank.com/challenges/py-hello-world/problem
"""

import sys

def main():
    N,T,M = map(int,sys.stdin.readline().split())
    print(N * T * M)

if __name__ == "__main__":
    main()
