

def main():
	n = int(input())
	s = input()

	s = swap(s, '012', '210')
	s = swap(s, '102', '012')
	s = swap(s, '201', '120')

	print(s)

def swap(s, a, b):
	i = 0
	while i < len(s):
		if s[i:i+3] == a:
			s = s[:i] + b + s[i+3:]
		i = i + 1
	return s

main()
