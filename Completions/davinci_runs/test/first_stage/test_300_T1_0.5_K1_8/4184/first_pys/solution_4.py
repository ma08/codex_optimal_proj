

N = int(input())
W = [int(i) for i in input().split()]

if N == 2:
    print(abs(W[0]-W[1]))
else:
    ans = 100 * 100
    for i in range(2**(N-1)):
        S1 = 0
        S2 = sum(W)
        for j in range(N-1):
            if i & (1 << j):
                S1 += W[j]
                S2 -= W[j]
        ans = min(ans, abs(S1-S2))
    print(ans)