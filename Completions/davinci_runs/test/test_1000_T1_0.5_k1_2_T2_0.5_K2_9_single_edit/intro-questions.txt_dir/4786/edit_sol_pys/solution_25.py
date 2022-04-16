#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 16:01:46 2019


@author: shashank
"""

def main():
    n = int(input())
    keywords = [input().lower().replace("-", " ") for _ in range(n)]
    similar = set()
    for i in range(n):
        for j in range(i+1, n):
            if keywords[i] == keywords[j]:
                similar.add(keywords[i])
    print(n - len(similar))

if __name__ == '__main__':
    main()
