

S = input()[::-1]

for i in range(len(S)-1):
    if S[i] == ' ':
        S = S[:i] + 'x' + S[i+1:]

print(S)
