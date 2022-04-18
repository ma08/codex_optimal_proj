
import sys

n = int(input())
a = list(map(int, input().split()))

stack = []
for i in range(n):
    stack.append(a[i])
    print(*stack[::-1])
