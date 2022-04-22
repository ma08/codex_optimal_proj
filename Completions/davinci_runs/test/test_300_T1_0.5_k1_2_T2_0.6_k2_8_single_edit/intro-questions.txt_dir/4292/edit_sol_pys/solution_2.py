import sys
from collections import Counter



N = int(input())
A = list(map(int, input().split()))
cnt = Counter(A)
ans = 0
for key, val in cnt.items():
    if key > val:
        ans += val
    elif key < val:
        ans += val - key
print(ans)
