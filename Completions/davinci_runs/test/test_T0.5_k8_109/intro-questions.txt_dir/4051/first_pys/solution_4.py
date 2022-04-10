

def ravioli_sort(arr):
	# print(arr)
	while len(arr) > 0:
		max_height = max(arr)
		max_index = arr.index(max_height)
		if max_index == len(arr)-1:
			return "NO"
		if max_height - arr[max_index+1] >= 2:
			return "NO"
		arr.pop(max_index)
	return "YES"

n = int(input())
arr = list(map(int, input().split()))
print(ravioli_sort(arr))