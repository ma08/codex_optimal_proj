# coding: utf-8


import sys
readline = sys.stdin.buffer.readline

n = int(readline())
a = readline()

# n = int(input())
# a = input()

print(a[:n//2])
