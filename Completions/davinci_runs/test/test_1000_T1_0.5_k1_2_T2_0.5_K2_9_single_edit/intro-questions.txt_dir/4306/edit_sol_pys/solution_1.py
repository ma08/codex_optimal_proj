
import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
a.sort()
ans = 0
for i in a:
    ans = max(ans, a.count(i) + a.count(i - 1) + a.count(i + 1))
print(ans)
