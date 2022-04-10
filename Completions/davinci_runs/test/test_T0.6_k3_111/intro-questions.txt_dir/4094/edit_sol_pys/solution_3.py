#!/usr/bin/env python3
import sys

k = int(sys.stdin.readline())

num = 7
count = 1
while True:
    if num % k == 0:
        print(count)
        break
    num = num * 10 + 7 # num = num * 10 + 7
    count += 1
