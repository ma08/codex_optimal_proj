

import itertools

n, m = map(int, input().split())
q = [list(map(int, input().split())) for i in range(m)]

possible_numbers = [str(i) for i in range(10)]

for i in range(m):
    s_i, c_i = q[i][0] - 1, str(q[i][1])
    possible_numbers[s_i] = c_i
    for j in range(10):
        if str(j) != c_i:
            possible_numbers[s_i] = possible_numbers[s_i].replace(str(j), '')

ans = -1
for i in itertools.product(*possible_numbers):
    i = int(''.join(i))
    if len(str(i)) == n and i >= 0:
        if ans == -1:
            ans = i
        else:
            ans = min(ans, i)
print(ans)

# Reference code
n, m = map(int, input().split())
q = [list(map(int, input().split())) for i in range(m)]

ans = -1
for i in range(1000, 10000):
    s = str(i)
    ok = True
    for j in range(m):
        if s[q[j][0]-1] != str(q[j][1]):
            ok = False
    if ok:
        ans = i
        break
print(ans)
