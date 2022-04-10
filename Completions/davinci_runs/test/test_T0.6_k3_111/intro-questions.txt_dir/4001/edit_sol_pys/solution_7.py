n = int(input())
s = input().split()
d = dict()
res = []
for i in s:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
for i in d:
    if d[i] % 2 != 0:
        res.append(int(i))
print(res[0], res[1])
