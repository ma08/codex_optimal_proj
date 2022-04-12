

# SOLUTION 
import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    if a == b:
        print(0)
    else:
        c = abs(a - b)
        if c % 10 == 0:
            print(c // 10)
        else:
            print(c // 10 + 1)
