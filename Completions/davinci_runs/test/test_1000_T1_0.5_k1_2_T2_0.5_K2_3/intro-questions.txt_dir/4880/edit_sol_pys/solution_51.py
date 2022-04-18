# -*- coding: utf-8 -*-

import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    keyword = sys.stdin.readline().strip()
    cipher = sys.stdin.readline().strip()
    plain = []
    for i in range(0, m):
        plain.append(chr((ord(cipher[i]) - ord(keyword[i % n])) % 26 + 97))
    print("".join(plain)) # 字符串连接函数

if __name__ == "__main__":
    main()
