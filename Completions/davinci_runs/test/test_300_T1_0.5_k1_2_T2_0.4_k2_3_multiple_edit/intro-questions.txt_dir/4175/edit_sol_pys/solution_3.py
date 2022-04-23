N, Q = map(int, input().split())
S = input()
l = [0] * (N + 1)
for i in range(N - 1):
    if S[i] == 'A' and S[i + 1] == 'C':
        l[i + 1] = l[i] + 1
    else:
        l[i + 1] = l[i]
for i in range(Q):
    l, r = map(int, input().split())
    print(l[r - 1] - l[l - 1])
