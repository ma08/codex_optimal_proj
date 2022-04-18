
S = input()
ans = 0
for i in range(len(S) - 2):
    if S[i:i + 3] == "ABC":
        ans += 1
print(ans)
