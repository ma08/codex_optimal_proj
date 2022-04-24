

def main():
	s = input()

	s = swap(s, '012', '120') #1
	s = swap(s, '102', '210') #2
	s = swap(s, '201', '012') #3

	print(s) #4

def swap(s, a, b):
	i = 0
	while i < len(s):
		if s[i:i+3] == a:
			s = s[:i] + b + s[i+3:]
		i = i + 1
	return s

main()
