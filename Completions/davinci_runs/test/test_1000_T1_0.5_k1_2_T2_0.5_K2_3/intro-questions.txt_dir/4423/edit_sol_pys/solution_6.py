N = int(input())
d = {}


for i in range(N):
    S, P = input().split()
    P = int(P)
    d[S] = d.get(S, []) + [(i + 1, P)]

for s in sorted(d.keys()):
    for i, P in sorted(d[s], key=lambda x: x[1], reverse=True):
        print(i)
