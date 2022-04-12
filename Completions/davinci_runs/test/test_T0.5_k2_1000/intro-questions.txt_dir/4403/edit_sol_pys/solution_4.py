S = str(input())

cnt = 0

for i in range(len(S)):
    if S[i] == "+":
        cnt += 1
    else:
        cnt -= 1

print(cnt)
