
import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
N = int(input())

count = 0
for i in range(1, N + 1):
    count += len(str(i)) % 2

print(count)
