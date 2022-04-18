

S = input()

cnt = 0
for i in range(len(S)):
    if i == 0:
        if S[i] == S[i+1]:
            cnt += 1
    elif i == len(S)-1:
        if S[i] == S[i-1]:
            cnt += 1
    else:
        if S[i] == S[i+1] or S[i] == S[i-1]:
            cnt += 1
print(cnt)