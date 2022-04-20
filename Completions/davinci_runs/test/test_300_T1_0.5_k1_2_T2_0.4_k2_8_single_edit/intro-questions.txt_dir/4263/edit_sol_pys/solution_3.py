

#S = input()
S = "ATCODER"
ans = 0

for i in range(len(S)):
    for j in range(i, len(S)):
        if S[i] != "A" and S[i] != "C" and S[i] != "G" and S[i] != "T":
        ans += 1
            break

print(ans)
