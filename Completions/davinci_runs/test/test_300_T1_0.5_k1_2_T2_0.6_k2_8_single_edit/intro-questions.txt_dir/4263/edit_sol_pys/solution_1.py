

# S = input()
S = "ATCODER"  # test

ans = 0

for i in range(len(S)):
    for j in range(i, len(S)):
        if S[j] == "A" or S[j] == "C" or S[j] == "G" or S[j] == "T":
            ans = max(ans, j-i+1)
        else:  # "N"
            break

print(ans)
