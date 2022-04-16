
N = int(input())
S = input()

cnt = 0
for i in range(N):
    if S[i] == 'R':
        cnt += 1

print(cnt)
