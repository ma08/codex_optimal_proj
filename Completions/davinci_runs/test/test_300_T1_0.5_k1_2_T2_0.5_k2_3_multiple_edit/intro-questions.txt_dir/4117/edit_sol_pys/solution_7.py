import sys
input = sys.stdin.readline



N, K = map(int, input().split())
h = list(map(int, input().split()))

print(min(h))
