

from collections import defaultdict
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a_dict = defaultdict(list)
for i, x in enumerate(a):
    a_dict[x].append(i)

b_dict = defaultdict(list)
for i, x in enumerate(b):
    b_dict[x].append(i)

c = [0] * n
for i in range(n):
    for j in a_dict[i]:
        for k in b_dict[n - i]:
            c[j] = k
            b_dict[n - i].remove(k)
            break
print(*c)