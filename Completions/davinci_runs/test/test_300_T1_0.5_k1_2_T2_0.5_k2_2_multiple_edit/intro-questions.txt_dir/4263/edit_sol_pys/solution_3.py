# -*- coding: utf-8 -*-
# AOJ
# ITP1_4_A
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_4_A

S = input()
#S = "ATCODER"
ans = 0

for i in range(len(S)):
    for j in range(i, len(S)):
        if S[i] == "A" or S[i] == "C" or S[i] == "G" or S[i] == "T":
            ans += 1
        else:
            break

print(ans)
