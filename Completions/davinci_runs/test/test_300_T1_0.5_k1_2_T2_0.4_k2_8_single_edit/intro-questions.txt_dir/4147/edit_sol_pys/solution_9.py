N = int(input())
S = input()
K = int(input())


ans = ''

for i in range(N):
    if S[i] == S[K - 1]:
        ans += S[i]
    else:
        ans += '*'
print(ans)
