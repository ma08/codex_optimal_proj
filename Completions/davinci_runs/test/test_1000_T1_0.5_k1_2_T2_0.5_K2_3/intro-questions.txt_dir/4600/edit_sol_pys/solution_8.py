
# -----Input Part-----
N, M = map(int, input().split())

# -----Process Part-----
result = [0] * N
penalty = [0] * N

for i in range(M):
    p, S = input().split()
    p = int(p) - 1
    if result[p] == 0:
        if S == "AC":
            result[p] = 1
        elif S == "WA":
            penalty[p] += 1

# -----Output Part-----
print(sum(result), sum(penalty)) 
