N, K = map(int, input().split())
A = list(map(int, input().split()))


if K in A:
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')

