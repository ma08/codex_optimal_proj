from sys import stdin

k, x = map(int, stdin.readline().split())

for i in range(max(x - k + 1, -1000000), min(x + k, 1000000) + 1):
    print(i, end=' ')
