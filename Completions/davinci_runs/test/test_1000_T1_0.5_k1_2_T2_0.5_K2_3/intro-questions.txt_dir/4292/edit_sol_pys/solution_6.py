import sys

n, k = map(int, sys.stdin.readline().split())  # n개의 수가 주어지고, k개의 수를 뽑는 것이다.
p = list(map(int, sys.stdin.readline().split()))

print(sum(sorted(p)[:k]))
