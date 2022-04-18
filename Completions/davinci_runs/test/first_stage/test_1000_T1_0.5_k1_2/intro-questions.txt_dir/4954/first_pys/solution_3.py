

def main():
	"""
	1. Read in the number of participants, budget, number of hotels, and number of weeks
	2. Read in the price for one person staying the weekend at the hotel for all hotels
	3. Read in the number of available beds for each hotel for each week
	4. For each hotel, for each week, check if the price is within budget, and if the number of available beds is greater than or equal to the number of participants
	5. Print the minimum cost of the stay for the group, or "stay home" if nothing can be found within the budget
	"""
	N, B, H, W = map(int, input().split())
	p = [int(input()) for _ in range(H)]
	a = [list(map(int, input().split())) for _ in range(H)]
	costs = []
	for hotel in range(H):
		for week in range(W):
			if p[hotel] * N <= B and a[hotel][week] >= N:
				costs.append(p[hotel] * N)
	if len(costs) > 0:
		print(min(costs))
	else:
		print("stay home")

if __name__ == "__main__":
	main()