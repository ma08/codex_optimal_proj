
N = int(input())
P = list(map(int, input().split()))

P_sorted = sorted(P)

for i in range(N):
    if P[i] == P_sorted[i]:
        continue
    else:
        P[i], P[P.index(P_sorted[i])] = P[P.index(P_sorted[i])], P[i]
        if P == P_sorted:
            print("YES")
            exit()

print("NO")
