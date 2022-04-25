
from collections import deque
from itertools import combinations

n, m = map(int, input().split())
a = []
b = []
for i in range(n):
    a.append(deque())
for i in range(n):
    a[i] = deque(map(int, input().split()))
for i in range(m):
    b.append(deque())
for i in range(m):
    b[i] = deque(map(int, input().split()))

def solve(a, b, n, m):
    if n == 1 or m == 1:
        return sum(a[0]) + sum(b[0])
    else:
        ans = 0
        for i in range(n):
            for j in range(m):
                ans = max(ans, a[i][j] + b[i][j])
        return ans

if __name__ == '__main__':
    print(solve(a, b, n, m))
