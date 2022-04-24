
import sys

def solve(n, s, d, m):
    count = 0
    for i in range(n):
        for j in range(i, n):
            if sum(s[i:j+1]) == d:
                count += 1
    return count

n = int(raw_input().strip())
s = map(int, raw_input().strip().split(' '))
d, m = raw_input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)
