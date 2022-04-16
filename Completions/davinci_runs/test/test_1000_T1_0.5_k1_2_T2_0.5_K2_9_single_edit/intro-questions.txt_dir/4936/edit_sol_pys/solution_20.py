

def main():
	n = int(input())
	temps = list(map(int, input().split()))

	max_temp = temps[0]
	day = 1

	for i in range(1, n):
		if temps[i] > max_temp:
			max_temp = temps[i]
			day = i + 1

		if temp > max_temp:
			max_temp = temp
			day = i + 1

	print(day, max_temp)

if __name__ == "__main__":
	main()
