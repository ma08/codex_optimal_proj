

import sys, string

s = sys.stdin.readline().strip()

count = 0
for c in string.ascii_lowercase:
	if s.count(c) > count:
		count = s.count(c)
		ans = c

print(ans)
