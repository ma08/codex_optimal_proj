# https://codeforces.com/problemset/problem/1294/A

T = int(input())

for _ in range(T):
    A, B, C, N = map(int, input().split())

    if N % 3 == 0:
        print('YES')
    else:
        print('NO')
