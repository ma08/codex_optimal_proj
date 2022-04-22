
S = input()
ans = 0

for i in range(len(S) - 2):
    if S[i] == "A" and S[i+1] == "C":
        ans += 1

print(ans)
