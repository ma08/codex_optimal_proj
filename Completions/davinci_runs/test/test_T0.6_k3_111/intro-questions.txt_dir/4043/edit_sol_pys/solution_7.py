

def main():
	n, d, k = [int(x) for x in input().split()]
	if d == 1:
		print("YES")
		for i in range(1, n):
			print(i, i + 1)
	elif d == 2:
		if k < 3:
			print("NO")
		else:
			print("YES")
			print(2, 3)
			print(3, 4)
			print(4, 5)
			print(5, 6)
			print(1, 2)
			print(1, 3)
			print(1, 4)
			print(1, 5)
			print(1, 6)
			print(1, 7)
			print(1, 8)
	elif d == 3:
		if k < 3:
			print("NO")
		else:
			print("YES")
			print(3, 4)
			print(4, 5)
			print(2, 3)
			print(2, 5)
			print(1, 2)
			print(1, 3)
			print(1, 4)
			print(1, 5)
			print(1, 6)
			print(1, 7)
			print(1, 8)
	elif d == 4:
		if k < 3:
			print("NO")
		else:
			print("YES")
			print(3, 4)
			print(4, 5)
			print(5, 6)
			print(2, 3)
			print(2, 5)
			print(2, 6)
			print(1, 2)
			print(1, 3)
			print(1, 4)
			print(1, 5)
			print(1, 6)
			print(1, 7)
			print(1, 8)
	elif d == 5:
		if k < 3:
			print("NO")
		else:
			print("YES")
			print(1, 2)
			print(3, 4)
			print(4, 5)
			print(5, 6)
			print(1, 3)
			print(1, 4)
			print(1, 5)
			print(1, 6)
			print(1, 7)
			print(1, 8)

if __name__ == '__main__':
	main()
