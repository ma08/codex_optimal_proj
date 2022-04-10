

def main():
	x1, y1, x2, y2 = [int(x) for x in input().split()]
	x3, y3, x4, y4 = [int(x) for x in input().split()]
	x5, y5, x6, y6 = [int(x) for x in input().split()]

	if x3 <= x1 and x4 >= x2 and y3 <= y1 and y4 >= y2:
		print("NO")
		return

	if x5 <= x1 and x6 >= x2 and y5 <= y1 and y6 >= y2:
		print("NO")
		return

	print("YES")

if __name__ == '__main__':
	main()