import math

def get_min_packages(n, k):
    if n == 1:
        return 1
    if k == 1:
        return n
    if k == 2:
        return int(math.ceil(n/2.0))
    if k == 3:
        return int(math.ceil(n/3.0))
    if k == 4:
        return int(math.ceil(n/4.0))
    return int(math.ceil(n/k))

t = int(input())
for i in range(t):
    n,k = map(int,input().split())
    print(get_min_packages(n,k))
