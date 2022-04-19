

import sys

def solve(string, sub, start, end):
	if start == end:
		return len(string) - end
	mid = (start + end) / 2
	if subsequence(string[:mid], sub):
		return solve(string, sub, start, mid)
	else:
		return solve(string, sub, mid + 1, end)

def subsequence(string, sub, i, j):
	if not sub:
		return True
	for c in string:
		if c == sub[i]:
			i += 1
			if i == len(sub):
				return True
	return False

sys.setrecursionlimit(100000)
print solve(raw_input(), raw_input(), 0, len(raw_input()))
