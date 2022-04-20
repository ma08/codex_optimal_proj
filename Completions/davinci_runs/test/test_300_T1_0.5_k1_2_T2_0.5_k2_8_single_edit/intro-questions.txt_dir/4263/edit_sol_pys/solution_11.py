

#S = input()
S = "ATCODER"
ans = 0

for i in range(len(S)):
    for j in range(i, len(S)):
        if S[j] != "A" and S[j] != "C" and S[j] != "G" and S[j] != "T":
    ans += 1
            break

print(ans)
