#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

def main():
    string = sys.stdin.readline().strip()
    for i in range(1, len(string)):
        if string[:i] * (len(string) // i) == string:  # noqa: E203
            print(i)
            break

main()
