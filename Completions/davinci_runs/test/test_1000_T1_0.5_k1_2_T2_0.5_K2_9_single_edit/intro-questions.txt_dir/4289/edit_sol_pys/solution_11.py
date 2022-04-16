
import sys
input = sys.stdin.readline
n = int(input())
h = [int(input()) for i in range(n)]

print(min(h) + max(h))
