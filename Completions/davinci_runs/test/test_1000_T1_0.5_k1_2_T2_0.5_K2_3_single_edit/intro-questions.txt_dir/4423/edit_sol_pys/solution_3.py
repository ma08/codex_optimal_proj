

n = int(input())
d = {}
for i in range(n):
    s, p = input().split()
    p = int(p)
    if s not in d.keys():
        d[s] = [p]
    else:
        d[s].append(p)

for s in d.keys():
    d[s] = sorted(d[s], reverse=True)

for s in sorted(d.keys(), reverse=True):
    for p in d[s]:
        print(s,p)
