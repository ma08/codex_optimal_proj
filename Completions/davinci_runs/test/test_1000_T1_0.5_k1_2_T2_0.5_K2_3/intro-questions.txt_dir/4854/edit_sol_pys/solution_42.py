import sys
n, c = map(int, sys.stdin.readline().split())
message = list(map(int, sys.stdin.readline().split()))
freq = [0] * (c + 1)

for i in message:
    freq[i] += 1
for i in range(c + 1):
    if freq[i]:
        print(str(i) * freq[i], end=' ') 
