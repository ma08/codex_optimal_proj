# -*- coding: utf-8 -*-

import sys

def main():
    n = int(sys.stdin.readline().rstrip())
    s = sys.stdin.readline().rstrip()
    #print(n)
    #print(s)
    #print(len(s))

    w_count = 0
    e_count = 0
    for i in range(len(s)):
        if s[i] == "W":
            w_count += 1
        if s[i] == "E":
            e_count += 1
    #print(w_count)
    #print(e_count)

    if w_count > e_count:
        print(e_count)
    else:
        print(w_count)

if __name__ == '__main__':
    main()
