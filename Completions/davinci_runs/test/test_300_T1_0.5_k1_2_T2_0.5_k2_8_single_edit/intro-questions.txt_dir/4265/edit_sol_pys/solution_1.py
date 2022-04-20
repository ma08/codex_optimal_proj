from collections import Counter


n = int(input())
a = list(map(int, input().split()))

ans = 0
for i in range(len(s)):
    if s[i] != t[i]:
        ans += 1

print(ans)
