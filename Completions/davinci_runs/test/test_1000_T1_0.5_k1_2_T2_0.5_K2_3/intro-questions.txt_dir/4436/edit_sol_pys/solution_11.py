

import sys


sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

n = int(input())
for i in range(n):
    number = int(input())
    if number % 2 == 0:
        print("YES")
        for j in range(2, number // 2):
            if number % j == 0:
                print(j, end=" ")
                number //= j
                break
        print(number)
    else:
        print("NO")
