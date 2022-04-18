
from itertools import combinations

def check(l, w, s):
    if l * w != len(s):
        return False
    for i in range(l):
        for j in range(w):
            if s[i * w + j] == '#':
                if i + 1 < l and s[(i + 1) * w + j] == '#':
                    continue
                elif j + 1 < w and s[i * w + j + 1] == '#':
                    continue
                else:
                    return False
    return True

n = int(input())
s = []
for i in range(n):
    s.append(input())

for i in range(1, n + 1):
    for j in range(1, n + 1):
        for comb in combinations(s, i * j):
            if check(i, j, ''.join(comb)):
                print(i, j)
                exit()
print('impossible')
