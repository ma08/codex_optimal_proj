

def carrots(N, P):
    carrots = P
    for _ in range(N):
        input()
    print(carrots)


N, P = map(int, input().split())  # noqa: E501
carrots(N, P)
