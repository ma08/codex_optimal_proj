

from itertools import permutations


a, b, x = map(int, input().split())

s = "0"*a + "1"*b + "2"

for i in range(a):
    for j in range(b):
        if i + j == x:
            print(s)
            exit()
        s = s[1:] + s[0]
