
S = input()
ans = 0

for i in range(len(S)-1):
    for j in range(i+1, len(S)):
        if S[i:j] == "A" or S[i:j] == "C" or S[i:j] == "G" or S[i:j] == "T":
            ans = max(ans, j-i)

print(ans)
