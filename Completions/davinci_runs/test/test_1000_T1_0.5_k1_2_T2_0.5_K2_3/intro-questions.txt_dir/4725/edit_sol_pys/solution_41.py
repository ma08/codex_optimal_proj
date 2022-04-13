#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def main():
    text = sys.stdin.readline().strip()
    if len(text) <= 2:
        print(0)
    else:
        chars = set()
        for i in range(len(text)):
            if text[i] not in chars:
                chars.add(text[i])
            if len(chars) > 2:
                print(i)
                return
        print(len(text))

if __name__ == '__main__':
    main()
