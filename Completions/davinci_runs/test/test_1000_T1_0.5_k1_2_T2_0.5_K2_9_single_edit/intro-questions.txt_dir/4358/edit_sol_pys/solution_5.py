
import sys
input = sys.stdin.readline
n = int(input()) - 1
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
ans = 0
for i in range(n):
    if a[i] == b[i] and b[i] == c[i]:
        ans += 0
    elif a[i] == b[i] or b[i] == c[i] or c[i] == a[i]:
        ans += 1
    else:
        ans += 2
print(ans)
