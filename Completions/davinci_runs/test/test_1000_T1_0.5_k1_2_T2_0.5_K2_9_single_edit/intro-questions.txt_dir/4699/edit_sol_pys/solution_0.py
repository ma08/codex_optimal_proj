
N = int(input())
S = input()
s = S[0]
ans = 1
for i in range(1, N):
    if S[i] != s:
        ans += 1
        s = S[i]
print(ans)
