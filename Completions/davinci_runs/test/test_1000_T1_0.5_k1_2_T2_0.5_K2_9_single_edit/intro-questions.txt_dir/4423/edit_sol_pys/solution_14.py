

n = int(input())
d = {}
for i in range(n):
    s, p = input().split()
    p = int(p)
    if s in d.keys():
        d[s].append(p)
    else:
        d[s] = [p]

for s in sorted(d.keys()):
    d[s].sort(reverse=True)

for s in sorted(d.keys()):
    for p in d[s]:
        print(s, p)
