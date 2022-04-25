
S = input()
ans = 0

for i in range(len(S) - 1):
    if S[i] == "A" or S[i] == "C" or S[i] == "G" or S[i] == "T":
        ans += 1
    else:
        ans = 0

print(ans)
