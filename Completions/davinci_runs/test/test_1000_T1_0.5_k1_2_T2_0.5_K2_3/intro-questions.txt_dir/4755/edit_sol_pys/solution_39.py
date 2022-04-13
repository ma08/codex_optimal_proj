
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
 
n, m = map(int, input().split())
a = list(map(int, input().split()))
 
a.sort()
 
ans = 0
for i in range(n):
    ans += a[i] * min(m, n-i)
 
print(ans)
