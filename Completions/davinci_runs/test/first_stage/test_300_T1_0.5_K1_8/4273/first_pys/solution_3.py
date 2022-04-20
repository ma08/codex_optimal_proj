

N = int(input())

S = []

for i in range(N):
    S.append(input())

cnt = 0

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if S[i][0] == "M" or S[i][0] == "A" or S[i][0] == "R" or S[i][0] == "C" or S[i][0] == "H":
                if S[j][0] == "M" or S[j][0] == "A" or S[j][0] == "R" or S[j][0] == "C" or S[j][0] == "H":
                    if S[k][0] == "M" or S[k][0] == "A" or S[k][0] == "R" or S[k][0] == "C" or S[k][0] == "H":
                        if S[i][0] != S[j][0] and S[j][0] != S[k][0] and S[k][0] != S[i][0]:
                            cnt += 1

print(cnt)