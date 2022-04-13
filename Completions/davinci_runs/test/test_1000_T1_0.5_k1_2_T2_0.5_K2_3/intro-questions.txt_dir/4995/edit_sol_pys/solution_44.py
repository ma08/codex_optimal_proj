

def main():
	n = int(input())
	s = 0
	for i in range(n):
		m, s1 = input().split()
		s += int(m) * 60 - int(s1)
	if s <= 0:
		print("measurement error!")
	else:
		print(s / (n * 60))

if __name__ == '__main__':
	main()
