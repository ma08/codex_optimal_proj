
N = int(input())

d = {}
for i in range(N):
    S, P = input().split()
    P = int(P)
    if S in d:
        d[S].append((i, P))
    else:
        d[S] = [(i + 1, P)]

for S in sorted(d.keys()):
    for i, P in sorted(d[S], key=lambda x: x[1], reverse=True):  # 名前が同じ場合は得点が高い順に出力
        print(i)
