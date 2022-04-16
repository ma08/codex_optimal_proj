

import sys

# If you are using Python 3.x, you can use the following import instead:
# from io import BytesIO

# If you are using Python 2.x, you can use the following import instead:
# from StringIO import StringIO

def solve(n, a, q):
    # Write your code here
    a.sort()
    for i in range(q):
        if n == 1:
            return a[0]
        elif n == 2:
            return a[1]
        else:
            return max(a[0] * a[1] * a[2], a[0] * a[1] + a[2])

q = int(input())
for query_number in range(q):
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(n, a, q))
