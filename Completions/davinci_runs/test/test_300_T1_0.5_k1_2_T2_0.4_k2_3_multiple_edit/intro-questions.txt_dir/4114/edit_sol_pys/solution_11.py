
import sys

N, M = list(map(int, sys.stdin.readline().split()))

a_b = []
for i in range(M):
    a_b.append(list(map(int, sys.stdin.readline().split())))

a_b.sort(key=lambda x: x[1])

count = 0
end = 0
for i in range(M):
    if a_b[i][0] >= end:
        end = a_b[i][1]
        count += 1

print(count)
