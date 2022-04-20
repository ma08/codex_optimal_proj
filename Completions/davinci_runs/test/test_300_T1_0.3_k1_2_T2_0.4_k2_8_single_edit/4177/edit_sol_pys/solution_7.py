
S = input()

for i in range(len(S)):
    S = S[:i] + 'x' + S[i+1:]
print(S)
