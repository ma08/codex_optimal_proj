# coding=utf-8

import sys


def input():
    return sys.stdin.readline()



letters = [0 for _ in range(26)]

for letter in input():
    letters[ord(letter) - ord('a')] += 1

print(sum(letter % 2 for letter in letters))
