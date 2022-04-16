# -----Library Part-----
import sys

# -----Input Part-----
N = int(input())
A = list(map(int, input().split()))

# -----Process Part-----
A.sort()
A.reverse()
count = 0

for i in range(M):
    p, S = input().split()
    p = int(p) - 1
    if S == "AC" and result[p] == 0:
        result[p] = 1
    elif S == "WA" and result[p] == 0:
        penalty[p] += 1

# -----Output Part-----
print(sum(result), sum(penalty))
