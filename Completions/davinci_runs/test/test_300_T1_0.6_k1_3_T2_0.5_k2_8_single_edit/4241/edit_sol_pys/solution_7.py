

S = input()
T = input()

slen = len(S)
tlen = len(T)

changes = [[0 for i in range(slen + 1)] for j in range(tlen + 1)]

for i in range(1, slen + 1):
    changes[0][i] = i

for j in range(1, tlen + 1):
    changes[j][0] = j

for j in range(1, tlen + 1):
    for i in range(1, slen + 1):
        if S[i-1] == T[j-1]:
            changes[j][i] = changes[j-1][i-1]
        else:
            changes[j][i] = min(changes[j-1][i], changes[j][i-1], changes[j-1][i-1]) + 1

print(changes[tlen][slen])
