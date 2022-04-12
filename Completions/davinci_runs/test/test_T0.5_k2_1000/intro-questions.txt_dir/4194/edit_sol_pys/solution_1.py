import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))

a.sort()

if a[-1] > n // m:
    print(-1)
    exit()

s = sum(a[:m])

print(n - s)
