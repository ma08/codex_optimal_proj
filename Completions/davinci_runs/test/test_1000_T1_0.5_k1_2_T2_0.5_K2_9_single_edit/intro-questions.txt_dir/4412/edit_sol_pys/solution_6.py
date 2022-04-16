
import sys

def solve(n, a):
    # Write your code here
    a.sort()
    if n == 1:
        return a[0]
    elif n == 2:
        return a[1]
        # print(a[0] * a[1] * a[2], a[0] * a[1] + a[2])
    else:
        return max(a[0] * a[1] * a[2], a[0] * a[1] + a[2])

q = int(input())
for query_number in range(q):
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(n, a))
