
s = input()
t = input()
N, M = len(s), len(t)

for i in range(M):
    for j in range(N):
        if s[j] == t[i]:
            print(t[i], end='')
        else:
            print('.', end='')
    print()
