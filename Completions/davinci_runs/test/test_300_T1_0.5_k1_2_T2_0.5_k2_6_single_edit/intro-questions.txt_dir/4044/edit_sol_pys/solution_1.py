
import sys
sys.setrecursionlimit(10**7)

a, b, x = map(int, input().split())

def dfs(s, a, b, x):
    if a == 0 and b == 0:
        if x == 0:
            print(s)
            sys.exit()
        else:
            return
    if x == 0:
        print(s + '0' * a + '1' * b)
        sys.exit()
    if a > 0:
        dfs(s + '0', a - 1, b, x)
    if b > 0:
        dfs(s + '1', a, b - 1, x - 1)

if x > a + b - 1 or x < abs(a - b):
    print(-1)
else:
    dfs('', a, b, x)
