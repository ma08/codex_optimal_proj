

from itertools import accumulate

# Solution 1
n, p, m = map(int, input().split())
names = [input() for _ in range(n)]
points = [int(input().split()[1]) for _ in range(m)]
s = accumulate(points)
for i, p in enumerate(s):
    if p >= n:
        print(*names[:i], sep='\n')
        break
else: print('No winner!')

# Solution 2
from itertools import accumulate

n, p, m = map(int, input().split())
names = [input() for _ in range(n)]
points = [int(input().split()[1]) for _ in range(m)]
s = accumulate(points)
for i, p in enumerate(s):
    if p >= n:
        print(*names[:i], sep='\n')
        break
else: print('No winner!')
