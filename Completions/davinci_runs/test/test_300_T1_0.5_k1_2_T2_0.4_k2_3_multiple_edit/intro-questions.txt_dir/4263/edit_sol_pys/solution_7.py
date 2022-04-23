
S = input()
ans = 0

for i in range(len(S) - 1):
    for j in range(i + 1, len(S)):
        if S[i] == "A" or S[i] == "C" or S[i] == "G" or S[i] == "T":
            ans += 1
        else:
            break

print(ans)
