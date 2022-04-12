#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    n = raw_input()
    n = n.split('-')
    for i in n:
        print(i[0], end="")
    print()

main()
