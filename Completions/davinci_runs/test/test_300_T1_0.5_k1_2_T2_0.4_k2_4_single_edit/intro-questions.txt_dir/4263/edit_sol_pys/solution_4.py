

S = input()
# S = "ATCODER"
ans = 0

    if S[i] == "A" or S[i] == "C" or S[i] == "G" or S[i] == "T":
        ans += 1
    else:
        continue

for i in range(len(S)):
    for j in range(i, len(S)):
        if S[j] == "A" or S[j] == "C" or S[j] == "G" or S[j] == "T":
            ans += 1
            if ans > i:
                ans = i
        else: 
            continue

print(ans)
