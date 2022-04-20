

N, A, B = map(int, input().split())

if N < 5:
    print(N * B)
else:
    print(B * 5 + (N - 5) * A)
