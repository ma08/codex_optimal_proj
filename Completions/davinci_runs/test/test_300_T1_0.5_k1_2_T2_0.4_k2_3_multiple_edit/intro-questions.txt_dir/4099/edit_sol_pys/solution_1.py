N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = list(input())

ans = 0
for i in range(N):
    if i < K:
        if T[i] == "r":
            ans += P
        elif T[i] == "s":
            ans += R
        elif T[i] == "p":
            ans += S
    else:
        if T[i] == "r":
            if T[i-K] == "r":
                T[i] = "n"
            else:
                ans += P
        elif T[i] == 's':
            if T[i-K] == 's':
                T[i] = 'n'
            else:
                ans += R
        elif T[i] == 'p':
            if T[i-K] == 'p':
                T[i] = 'n'
            else:
                ans += S

print(ans)
