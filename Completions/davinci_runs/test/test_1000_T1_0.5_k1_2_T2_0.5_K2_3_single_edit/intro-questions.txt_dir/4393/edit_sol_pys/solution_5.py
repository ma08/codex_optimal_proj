import sys
input = sys.stdin.readline


n = int(input()) 
a = list(map(int, input().split()))

ans = 0
for i in range(n-1):
    if a[i] == a[i+1]:
        ans += 1
        a[i+1] = 0

print(ans)
