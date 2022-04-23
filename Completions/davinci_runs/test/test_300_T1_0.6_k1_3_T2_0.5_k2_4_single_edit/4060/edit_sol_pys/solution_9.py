from collections import Counter


s = input()
s = s.lower()
s = s.replace(' ', '')
c = Counter(s)
max_ = max(c.values())
res = [i for i in c if c[i] == max_]
print(sorted(res)[0])
