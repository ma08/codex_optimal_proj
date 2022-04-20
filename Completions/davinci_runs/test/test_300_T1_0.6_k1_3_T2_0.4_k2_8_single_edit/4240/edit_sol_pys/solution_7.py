

from collections import defaultdict
from sys import stdin

n, m = map(int, stdin.readline().rstrip().split())
a = list(map(int, stdin.readline().rstrip().split()))
b = list(map(int, stdin.readline().rstrip().split()))
c = list(map(int, stdin.readline().rstrip().split()))

a_dict = defaultdict(int)
b_dict = defaultdict(int)
c_dict = defaultdict(int)

for i in range(n):
    a_dict[a[i]] += 1
for i in range(m):
    b_dict[b[i]] += 1
    c_dict[c[i]] += 1

for a_key, a_value in a_dict.items():
    for b_key, b_value in b_dict.items():
        c_value = c_dict[a_key ^ b_key]
        if c_value != a_value * b_value:
            print("No")
            exit()

print("Yes")
