

def main():
	n = int(input())  # number of days
	temps = list(map(int, input().split()))  # list of temperatures

	max_temp = 0  # max temperature
	day = 0  # day of max temperature

	for i in range(n - 2):
		temp = max(temps[i], temps[i + 1], temps[i + 2])  # max temperature of the day

		if temp > max_temp:  # if the temperature is greater than the current max temperature
			max_temp = temp
			day = i + 1

	print(day, max_temp)

if __name__ == "__main__":
	main()
