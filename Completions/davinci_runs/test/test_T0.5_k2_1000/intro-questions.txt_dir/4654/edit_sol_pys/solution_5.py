# coding=utf-8


def f(n, k):
    if n % 2 == 0:
        return 'YES'
    return 'NO'


t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    print(f(n, k))
