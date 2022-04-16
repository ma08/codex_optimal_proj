
n = int(input())
d = {}
for i in range(n):
    s, p = input().split()
    p = int(p)
    d[s] = d.get(s, []) + [p]

for s in sorted(d.keys()):
    d[s].sort(reverse=True)

for s in sorted(d.keys()):
    for p in d[s]:
        print(p)
