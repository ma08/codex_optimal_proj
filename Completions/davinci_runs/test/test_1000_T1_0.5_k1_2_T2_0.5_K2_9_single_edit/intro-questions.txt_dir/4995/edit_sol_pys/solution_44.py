

def main():
	n = int(input())
	s = 0
	for i in range(n):
		m, s1 = map(int, input().split())
		s += m * 60 - s1
	if s <= 0:
		print("measurement error")  # noqa: T001
	else:
		print(s / (n * 60))  # noqa: T001

if __name__ == '__main__':
	main()
