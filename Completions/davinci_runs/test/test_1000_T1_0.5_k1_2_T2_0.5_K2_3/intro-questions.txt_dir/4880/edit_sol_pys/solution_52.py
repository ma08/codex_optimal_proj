#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/2/23 下午11:01
# @Author  : simon
# @File    : file.py
# @Software: PyCharm Community Edition

import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    last_n = sys.stdin.readline().strip()[-n:].lower()
    ciphertext = sys.stdin.readline().strip()
    print(last_n)
    plaintext = ""
    for i in range(m):
        plaintext += chr((ord(ciphertext[i]) - ord(last_n[i % n]) + 26) % 26 + ord('a'))
        if i >= n - 1:
            last_n += plaintext[i]
    print(plaintext)

if __name__ == '__main__':
    main()
