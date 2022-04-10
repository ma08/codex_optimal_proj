

def solve(s, m, b):
	"""
	>>> solve('abac', 3, [2, 1, 0])
	'aac'
	>>> solve('abc', 1, [0])
	'b'
	>>> solve('abba', 3, [1, 0, 1])
	'aba'
	>>> solve('ecodsefr', 10, [38, 13, 24, 14, 11, 5, 3, 24, 17, 0])
	'codeforces'
	"""
	s = list(s)
	s.sort()
	res = ''

	for i, v in enumerate(b):
		idx, s = get_idx(s, v)
		res += s[idx]
		del s[idx]

	return res

def get_idx(s, b):
	"""
	>>> get_idx(['a', 'b', 'c'], 0) == (0, ['a', 'b', 'c'])
	True
	>>> get_idx(['a', 'b', 'c'], 1) == (1, ['a', 'b', 'c'])
	True
	>>> get_idx(['a', 'b', 'c'], 2) == (2, ['a', 'b', 'c'])
	True
	"""
	idx = b % len(s)
	return idx, s

if __name__ == '__main__':
	q = int(input())
	for i in range(q):
		s = input()
		m = int(input())
		b = [int(x) for x in input().split()]
		print(solve(s, m, b))
