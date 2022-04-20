

N, L = map(int, input().split())

print(sum(list(range(L, L+N))) - (L+N-1))