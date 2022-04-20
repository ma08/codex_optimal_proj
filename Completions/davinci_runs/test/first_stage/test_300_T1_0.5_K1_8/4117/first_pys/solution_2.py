

import sys
read = sys.stdin.readline

N = int(read())
L = list(map(int, read().split()))

count = 0

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if L[i] != L[j] and L[j] != L[k] and L[k] != L[i] and L[i] + L[j] > L[k] and L[j] + L[k] > L[i] and L[k] + L[i] > L[j]:
                count += 1

print(count)