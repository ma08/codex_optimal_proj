# https://open.kattis.com/problems/filip

import sys

numbers = sys.stdin.readline().split()

numbers[0] = numbers[0][::-1]
numbers[1] = numbers[1][::-1]

if int(numbers[0]) > int(numbers[1]):
    print(numbers[0])
else: 
    print(numbers[1])
