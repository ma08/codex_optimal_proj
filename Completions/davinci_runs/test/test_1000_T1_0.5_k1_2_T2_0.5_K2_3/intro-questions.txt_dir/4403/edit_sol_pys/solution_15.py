
S = str(input())
cnt = 0

for i in range(len(S)):
    if S[i] == "+":
        cnt += 1
    elif S[i] == "-":
        cnt -= 1

print(cnt)
