


def cheese_type(cheese):
	if cheese.lower() == "brie" or cheese.lower() == "camembert" or cheese.lower() == "feta" or cheese.lower() == "goat" or cheese.lower() == "muenster":
		return "soft"
	elif cheese.lower() == "asiago" or cheese.lower() == "cheddar" or cheese.lower() == "gouda" or cheese.lower() == "swiss" or cheese.lower() == "parmesan" or cheese.lower() == "emmental" or cheese.lower() == "edam" or cheese.lower() == "colby" or cheese.lower() == "gruyere":
		return "hard"

def main():
	n = int(input())
	cheeses = []
	cheese_count = {}
	for i in range(n):
		line = input().split()
		cheese = line[0]
		cheeses.append(cheese)
		cheese_count[cheese] = cheese_type(cheese)
	count = 0
	for i in range(n):
		if cheese_count[cheeses[i]] == "soft":
			count += 1
	print(count)

main()