

N = int(input())

d = {}
for i in range(N):
    S, P = input().split()
    P = int(P)
    if S in d:
        d[S].append((i + 1, P))
    else:
        d[S] = [(i + 1, P)]

for s in sorted(d.keys()):
    for i, _ in sorted(d[s], key=lambda x: x[1], reverse=True):
        print(i)
