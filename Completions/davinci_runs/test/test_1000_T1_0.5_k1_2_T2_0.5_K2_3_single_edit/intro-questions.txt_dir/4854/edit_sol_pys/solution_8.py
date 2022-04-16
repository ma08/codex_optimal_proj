
import sys

n, c = map(int, sys.stdin.readline().split())

message = list(map(int, sys.stdin.readline().split()))

freq = [0] * (c + 1)

for i in message:
    freq[i] += 1

for i in range(len(freq)):
    if freq[i] > 0:
        print(str(i) * freq[i], end=' ')
