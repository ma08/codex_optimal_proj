

from sys import stdin

k, x = map(int, stdin.readline().split())

for i in range(k-1):
    print(x-i, end=" ")
print(x+k-1)