#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

def main():
    for line in sys.stdin:
        string = line.strip()
        for i in range(1, len(string)):
            if string[:i] * (len(string) // i) == string:
                print(i)
                break

main()
