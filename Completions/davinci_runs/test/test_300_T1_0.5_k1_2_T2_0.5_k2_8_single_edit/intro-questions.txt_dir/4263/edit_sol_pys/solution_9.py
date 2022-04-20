

S = input()
#S = "ATCODER"
ans = 0

for i in range(len(S)):
    for j in range(i, len(S)):
        if S[j] == "A" or S[j] == "C" or S[j] == "G" or S[j] == "T":
            ans += 1
        else:
            j += 1

print(ans)
