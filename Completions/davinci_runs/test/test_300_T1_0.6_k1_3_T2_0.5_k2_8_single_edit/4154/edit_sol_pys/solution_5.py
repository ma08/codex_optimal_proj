

N, A = map(int, input().split())
X = list(map(int, input().split()))

L_min = min(L)
R_max = max(R)
print(R_max - L_min + 1)
