#coding:utf-8

import sys

def main():
    n = int(input())
    s = input()
    if s[0] == "S" and s[n-1] == "F":
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()
