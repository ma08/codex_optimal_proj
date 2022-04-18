import sys
input = sys.stdin.readline


n = int(input())
a = list(map(int, input().split()))

a = sorted(a)

ans = a[-1] - a[0]

for i in range(n-1):
    if ans > a[i+1] - a[i]:
        ans = a[i+1] - a[i]

print(ans)
