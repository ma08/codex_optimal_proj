

def main():
	n = int(input())
	s = input()

	s = swap(s, '012', '120', 0)
	s = swap(s, '102', '210', 0)
	s = swap(s, '201', '012', 0)

	print(s)

def swap(s, a, b, i):
	if i < len(s):
		if s[i:i+3] == a:
			s = s[:i] + b + s[i+3:]
		return swap(s, a, b, i + 1)
	else:
		return s

main()
