# -*- coding: utf-8 -*-
# AtCoder Beginner Contest
# Problem A

S = input()

cnt = 0
for i in range(len(S)):
    if i == 0 and S[i] == S[i+1]:
        cnt += 1
    elif i == len(S)-1 and S[i] == S[i-1]:
        cnt += 1
    else:
        if S[i-1] != S[i] != S[i+1]:
            cnt += 1
print(cnt)
