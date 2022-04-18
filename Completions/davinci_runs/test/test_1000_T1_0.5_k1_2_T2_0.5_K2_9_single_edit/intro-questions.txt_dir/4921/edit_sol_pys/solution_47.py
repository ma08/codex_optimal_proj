#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

def main():
    words = []
    for line in sys.stdin:
        line = line.strip().split()
        for word in line:
            if word.lower() not in words:
                words.append(word.lower())
                print(word.lower(), end=' ')
            else:
                print('.', end=' ')
        print('')

main()
