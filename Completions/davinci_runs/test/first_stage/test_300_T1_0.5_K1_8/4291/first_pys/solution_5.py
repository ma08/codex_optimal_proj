

N, Q = map(int, input().split())
S = input()

for i in range(Q):
    l, r = map(int, input().split())
    print(S[l-1:r-1].count('AC'))