

def main():
	n = int(input())
	t = input()
	s = ""
	for i in range(n, 0, -1):
		s += t[n-i:n-i+i]
	print(s)

if __name__ == '__main__':
	main()