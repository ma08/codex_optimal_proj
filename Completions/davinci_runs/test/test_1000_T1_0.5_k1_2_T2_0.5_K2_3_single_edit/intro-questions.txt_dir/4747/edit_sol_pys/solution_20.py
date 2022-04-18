
from collections import Counter
n = int(input())
arr = list(map(int, input().split()))
counts = Counter(arr)
for i in range(n):
    if counts[arr[i]] == 1:
        print(arr[i])
        break
