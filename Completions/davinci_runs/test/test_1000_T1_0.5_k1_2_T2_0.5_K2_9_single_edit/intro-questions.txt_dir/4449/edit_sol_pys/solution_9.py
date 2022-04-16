
# Solution 1

import sys

def find_min_time(n, a, b, c):
    min_time = sys.maxsize
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i != j and j != k and i != k:
                    time = abs(a[i]-b[j]) + abs(b[j]-c[k]) + abs(c[k]-a[i])
                    min_time = min(min_time, time)
    return min_time

q = int(input())
for _ in range(q):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    print(find_min_time(n, a, b, c))

# Solution 2

import sys

def find_min_time(n, a, b, c):
    a.sort()
    b.sort()
    c.sort()
    min_time = sys.maxsize
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i != j and j != k and i != k:
                    time = abs(a[i]-b[j]) + abs(b[j]-c[k]) + abs(c[k]-a[i])
                    min_time = min(min_time, time)
    return min_time

q = int(input())
for _ in range(q):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    print(find_min_time(n, a, b, c))
