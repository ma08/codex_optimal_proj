

from collections import Counter

s = input()
t = input()

s_count = Counter(s)
t_count = Counter(t)

for k, v in t_count.items():
    if k not in s_count:
        print(len(t))
        exit()
    else:
        s_count[k] -= v

print(sum(map(abs, s_count.values())))