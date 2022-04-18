

S = input()
#S = "ATCODER"
ans = 0

for j in range(len(S)):
    if S[j] == "A" or S[j] == "C" or S[j] == "G" or S[j] == "T":
        ans += 1
    else:
        ans = 0

print(ans)
