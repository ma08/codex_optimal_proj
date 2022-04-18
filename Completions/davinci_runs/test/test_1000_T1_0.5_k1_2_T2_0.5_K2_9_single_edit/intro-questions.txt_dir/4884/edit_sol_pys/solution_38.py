

def carrots(N, P, L):
    carrots = P
    for i in range(N):
        L[i] = input()
    print(carrots)

N, P = map(int, input().split())
L = [None]*N
carrots(N, P, L)
