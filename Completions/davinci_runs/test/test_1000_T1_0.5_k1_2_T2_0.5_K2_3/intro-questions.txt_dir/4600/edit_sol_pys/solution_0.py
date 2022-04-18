

# -----Input Part----- #
N, M = map(int, input().split())

# -----Process Part----- #
result = [0] * N
penalty = [0] * N

for i in range(M):
    p, S = input().split()
    p = int(p) - 1
    if S == "AC" and result[p] == 0:
        result[p] = 1
    elif S == "WA" and result[p] == 0:
        penalty[p] += 1

# -----Output Part----- #





print(sum(result), sum(penalty))
