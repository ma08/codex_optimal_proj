

# --- Solution 1 ---

def ravioli_sort(n,a):
	# If there is only one element, it is already sorted
	if n == 1:
		return "YES"
	# If there are two elements, check if they are sorted
	if n == 2:
		if a[0] > a[1]:
			return "NO"
		else:
			return "YES"
	# If there are more than two elements, check if they are sorted
	if n > 2:
		for i in range(n-1):
			if a[i] > a[i+1]:
				return "NO"
		return "YES"

# Get number of elements
n = int(input())

# Get elements
a = [int(i) for i in input().split()]

# Check if array is sorted
print(ravioli_sort(n,a))