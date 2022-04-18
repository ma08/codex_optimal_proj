import sys

sys.stdin = open('input.txt')


N = int(input())

print(sum(range(1, N+1)))
