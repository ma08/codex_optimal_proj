from collections import Counter

N = int(input())
H = list(map(int, input().split()))

cnt = Counter(H)
to_del = [k for k, v in cnt.items() if v > 1]
ans = 0
for i in range(N):
    if H[i] not in to_del:
        ans += 1
print(ans)
