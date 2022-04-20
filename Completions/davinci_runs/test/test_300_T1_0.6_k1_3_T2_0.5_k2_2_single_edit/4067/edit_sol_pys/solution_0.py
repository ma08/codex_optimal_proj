

def main():
	n = int(input())
	s = input()

	s = swap(s, '012', '120', 3)
	s = swap(s, '102', '210', 3)
	s = swap(s, '201', '012', 3)

	print(s)

def swap(s, a, b, n):
	i = 0
	while i < len(s):
		if s[i:i+n] == a:
			s = s[:i] + b + s[i+n:]
		i = i + 1
	return s

main()
