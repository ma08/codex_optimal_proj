

import sys

n = int(input())
numbers = [int(i) for i in input().split()]

numbers.sort()

if numbers[0] == numbers[1]:
    print(numbers[2])
else:
    print(numbers[0])
