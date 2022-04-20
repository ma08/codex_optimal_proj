

import sys
sys.stdin = open('input.txt', 'r')

def find(s, t):
	l = 0
	r = len(s)
	while l < r:
		m = (l + r) // 2
		if s[m] == t:
			return m
		elif s[m] > t:
			r = m
		else:
			l = m + 1
	return -1

s = input()
t = input()

i = 0
while i < len(t):
	pos = find(s[i:], t[i])
	if pos == -1:
		break
	else:
		i += pos + 1

print(len(t) - i)