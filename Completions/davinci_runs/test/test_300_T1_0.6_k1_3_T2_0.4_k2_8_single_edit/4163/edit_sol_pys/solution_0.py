

def main():
	N = int(input())
	count = 0
	for i in range(N):
		d1, d2 = map(int, input().split(" "))
		if d1 == d2:
			count += 1
		else:
			count = 0
		if count >= 3:
			break
	print("Yes" if count >= 3 else "No")

if __name__ == "__main__":
	main()
