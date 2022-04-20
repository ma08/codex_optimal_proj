n = int(input())
d = {}
for i in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    d[name] = scores
name = input()
s = d[name]
avg = sum(s) / len(s)
print('%.2f' % avg)


