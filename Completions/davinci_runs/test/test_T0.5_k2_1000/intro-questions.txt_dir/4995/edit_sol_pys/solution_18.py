

def main():
	n = int(input())
	s = 0
	for i in range(n):
		m, s1 = map(int, input().split())  # m - minutes, s1 - seconds
		s += m * 60 - s1  # s - seconds
	if s <= 0:
		print("measurement error")
	else:
		print(s / (n * 60))

if __name__ == '__main__':
	main()
