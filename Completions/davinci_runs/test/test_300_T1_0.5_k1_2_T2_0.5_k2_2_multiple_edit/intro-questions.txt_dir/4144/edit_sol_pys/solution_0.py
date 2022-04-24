N, K = map(int, input().split())
A = list(map(int, input().split()))


max_a = max(A)

if max_a < K:
    print('IMPOSSIBLE')
    exit()

if max_a == K:
    print('POSSIBLE')
    exit()

if K % 2 == 1:
    print('IMPOSSIBLE')
    exit()

if K % 2 == 0:
    if K in A:
        print('POSSIBLE')
        exit()

    for a in A:
        if a % 2 == 0:
            print('POSSIBLE')
            exit()

    print('IMPOSSIBLE')
    exit()

