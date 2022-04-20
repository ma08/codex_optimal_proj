
N = int(input())
S = input()
ans = 0
for i in range(N):
    if S[i] == ".":
        ans += 1
print(ans)
