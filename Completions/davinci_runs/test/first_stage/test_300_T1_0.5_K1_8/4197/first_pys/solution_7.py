

def main():
	"""
	Read N, A_i and print the student numbers of the students in the order the students entered the classroom.
	"""
	n = int(input())
	a_i = list(map(int, input().split()))
	
	a_i.sort(key=lambda x: x)
	
	print(*a_i)

if __name__ == '__main__':
	main()