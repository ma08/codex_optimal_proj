#!/usr/bin/env python
# -*- coding: utf-8 -*-



def main(input_file):
    with open(input_file, 'r') as f:
        for line in f:
            line = line.rstrip()
            print(line)

if __name__ == '__main__':
    main()
