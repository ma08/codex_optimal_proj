
# https://www.codechef.com/problems/SORTING
# SOLUTION
t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    p = list(map(int, input().split()))

    # if we can sort the array, then we can only swap the adjacent elements
    # but we can swap them any number of times
    # so we can sort the array in 2 steps:
    # 1. sort the array
    # 2. swap the adjacent elements in p
    # if we can sort the array, then we can swap the adjacent elements in p
    # if we can swap the adjacent elements in p, then we can sort the array
    a.sort()
    for i in range(m - 1):
        if p[i] + 1 == p[i + 1]:
            a[p[i]], a[p[i] + 1] = a[p[i] + 1], a[p[i]]
    print("YES" if all(a[i] <= a[i + 1] for i in range(n - 1)) else "NO") 
