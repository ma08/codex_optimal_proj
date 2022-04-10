

def main():
	n = int(input())
	a = list(map(int, input().split()))
	
	# Initialize a list of lists, each sublist containing the number of raviolis in a stack
	stacks = []
	for i in range(n):
		stacks.append([a[i]])
	
	# Sort the stacks in descending order
	stacks.sort(key = lambda x: x[0], reverse = True)
	
	# Check if the raviolis will slide down and make the sorting wrong
	for i in range(len(stacks)-1):
		if stacks[i][0] - stacks[i+1][0] > 1:
			print("NO")
			return
	
	print("YES")
	return

main()