

s = "10 ghost mummy witch demon demon demon demon demon demon demon"
s = s.split()

n = int(s[0])
s = s[1:]

d = {}

for i in s:
    d[i] = d.get(i, 0) + 1

m = max(d.values())

for k, v in d.items():
    if v == m:
        print(k)
