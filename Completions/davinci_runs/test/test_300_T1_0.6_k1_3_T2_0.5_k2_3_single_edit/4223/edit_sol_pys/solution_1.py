import sys
sys.setrecursionlimit(10**7)


n = int(input())
a = list(map(int, input().split()))

def f(i, a):
    if i == n:
        return []
    if a[i] == 0:
        return [[1, i]] + f(i+1, a)
    else:
        return f(i+1, a)

def g(i, a):
    if i == n:
        return []
    if a[i] == 1:
        return [[0, i]] + g(i+1, a)
    else:
        return g(i+1, a)

a = f(0, a) + g(0, a)

print(len(a))
for i, j in a:
    print(i, j+1)
