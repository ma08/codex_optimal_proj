# coding: utf-8

import sys

def main():
    s = sys.stdin.readline().rstrip()
    t = sys.stdin.readline().rstrip()
    if s == t:
        print("same")
    elif s.lower() == t.lower():
        print("case-insensitive")
    else:
        print("different")

if __name__ == '__main__':
    main()
