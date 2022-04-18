

from collections import Counter


N, K = map(int, input().split())
A = list(map(int, input().split()))

counter = Counter(A)
ans = 0
for key, value in counter.items():
    if value <= K:
        ans += 1
print(ans)
