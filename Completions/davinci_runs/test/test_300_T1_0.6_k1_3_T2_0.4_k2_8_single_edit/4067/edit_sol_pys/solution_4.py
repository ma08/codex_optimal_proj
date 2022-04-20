

def main():
	n = int(input())
	s = input()

	s = swap(s, '012', '120', n)
	s = swap(s, '102', '210', n)
	s = swap(s, '201', '012', n)

	print(s)

def swap(s, a, b, n):
	i = 0
	while i < n - 2:
		if s[i:i+3] == a:
			s = s[:i] + b + s[i+3:]
		i = i + 1
	return s

main()
