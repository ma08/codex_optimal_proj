

n = int(input())
d = {}
for i in range(n):
    s, p = input().split()
    p = int(p)
    if s not in d.keys():
        d[s] = [p]
    else:
        d[s].append(p)
print(d)
for s in sorted(d.keys()):
    d[s].sort(reverse=True)
print(d)
for s in sorted(d.keys()):
    for i in d[s]:
        print(i)
