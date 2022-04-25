
from collections import Counter

n = int(input())
s = input()
c = Counter(s)
ans = c['R'] * c['G'] * c['B']
print(ans)
