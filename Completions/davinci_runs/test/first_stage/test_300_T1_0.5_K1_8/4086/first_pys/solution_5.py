

import sys

def get_rightmost_index(array, value):
	index = -1
	for i in range(len(array)):
		if array[i] == value:
			index = i
	return index

def remove_duplicates(array):
	unique_array = []
	for i in range(len(array)):
		if array[i] not in unique_array:
			unique_array.append(array[i])
	return unique_array

def main():
	array_size = int(sys.stdin.readline())
	array = sys.stdin.readline().split(" ")

	unique_array = remove_duplicates(array)

	print(len(unique_array))
	for i in range(len(unique_array)):
		sys.stdout.write(unique_array[i] + " ")

if __name__ == "__main__":
	main()