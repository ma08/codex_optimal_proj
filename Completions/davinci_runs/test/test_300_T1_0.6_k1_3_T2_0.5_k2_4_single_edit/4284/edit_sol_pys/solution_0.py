import sys

sys.stdin = open('input.txt')

q = int(input())
for _ in range(q):
    k, n, a, b = map(int, input().split())
    if k < a and k < b:
        print(-1)
    elif k < a:
        print(k//b)
    elif k < a+b:
        print(1)
    else:
        print(min((k-a)//b + 1, n))
