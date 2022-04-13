

def main():
	n = int(input())
	s = 0
	for i in range(n):
		h, m = map(int, input().split())
		s += h * 60 + m
	if s <= 0:
		print("measurement error")
	else:
		print(round(s / (n * 60), 2))

if __name__ == '__main__':
	main()
