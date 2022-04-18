

S = input() #S = "ATCODER"

ans = 1

for i in range(1, len(S)):
    if S[i] == "A" or S[i] == "C" or S[i] == "G" or S[i] == "T":
        if S[i] == S[i-1]:
            ans += 1
    else:
        ans = 1

print(ans)
