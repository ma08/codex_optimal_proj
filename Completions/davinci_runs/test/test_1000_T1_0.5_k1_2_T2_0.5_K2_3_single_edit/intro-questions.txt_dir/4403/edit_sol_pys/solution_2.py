
S = str(input())
cnt = S.count("+")

for i in range(len(S)):
    if S[i] == "-":
        cnt -= 2

print(cnt)
