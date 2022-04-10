

def find_min_operations(a, b, c):
	n1 = a
	n2 = b
	n3 = c
	n1_operations = 0
	n2_operations = 0
	n3_operations = 0
	if n1 * 2 == n2 and n2 * 2 == n3:
		return [0, n1, n2, n3], n1, n2, n3
	elif n1 * 2 == n2:
		n1_operations = n2 - n1
		n2_operations = n3 - n2
	elif n2 * 2 == n3:
		n2_operations = n2 - n1
		n3_operations = n3 - n2
	else:
		n1_operations = n2 - n1
		n3_operations = n3 - n2
	if n1_operations % 2 == 0 and n3_operations % 2 == 0:
		n2_operations = n2_operations + n1_operations // 2
		n1_operations = n1_operations // 2
		n3_operations = n3_operations // 2
	elif n1_operations % 2 == 0:
		n2_operations = n2_operations + n1_operations // 2
		n1_operations = n1_operations // 2
		n3_operations = n3_operations // 2
	elif n3_operations % 2 == 0:
		n2_operations = n2_operations + n3_operations // 2
		n1_operations = n1_operations // 2
		n3_operations = n3_operations // 2
	else:
		n2_operations = n2_operations + n1_operations // 2
		n1_operations = n1_operations // 2
		n3_operations = n3_operations // 2
	n1 = n1 + n1_operations
	n2 = n2 + n2_operations
	n3 = n3 + n3_operations
	# print(n1, n2, n3)
	return [n1_operations + n2_operations + n3_operations, n1, n2, n3], n1, n2, n3

t = int(input())
for i in range(t):
	a, b, c = list(map(int, input().split()))
	# print(a, b, c)
	res, n1, n2, n3 = find_min_operations(a, b, c)[0]
	print(res)
	print(n1, n2, n3)
