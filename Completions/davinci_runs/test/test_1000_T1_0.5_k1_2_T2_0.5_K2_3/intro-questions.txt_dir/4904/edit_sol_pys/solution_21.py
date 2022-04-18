#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def main():
    score = {'A': 0, 'B': 0, 'C': 0}
    for i in sys.stdin.readline().strip():
        if i == 'A' or i == 'B' or i == 'C':
            score[i] += 1
        if score['A'] == 11 and score['B'] == 10 and score['C'] == 10:
            score['A'] -= 1
        if score['B'] == 11 and score['A'] == 10 and score['C'] == 10:
            score['B'] -= 1
        if score['C'] == 11 and score['A'] == 10 and score['B'] == 10:
            score['C'] -= 1
        if score['A'] >= 11 and score['B'] < score['A'] - 1 and score['C'] < score['A'] - 1:
            print('A')
            break
        if score['C'] >= 11 and score['A'] < score['C'] - 1 and score['B'] < score['C'] - 1:
            print('B')
            break
        if score['B'] >= 11 and score['A'] < score['B'] - 1 and score['C'] < score['B'] - 1:
            print('B')
            break
    else:
        print('C')

if __name__ == '__main__':
    main()
