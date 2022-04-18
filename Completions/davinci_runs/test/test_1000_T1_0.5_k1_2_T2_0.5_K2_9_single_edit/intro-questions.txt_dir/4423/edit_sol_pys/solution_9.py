

n = int(input())
d = {}
for i in range(n):
    s, p = input().split()
    p = int(p)
    if s not in d:
        d[s] = [p]
    else:
        d[s].append(p)

for s in sorted(d):
    d[s].sort(reverse=True)

for s in sorted(d):
    for p in d[s]:
        print(s, p)
