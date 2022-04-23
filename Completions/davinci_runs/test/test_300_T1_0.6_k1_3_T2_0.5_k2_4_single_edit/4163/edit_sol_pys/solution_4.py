

def main():
	N = int(input())
	count = 0
	for i in range(N):
		a, b = map(int, input().split())
		if a == b:
			count += 1
		else:
			count = 0
		if count >= 3:
			break
	print("Yes" if count >= 3 else "No")

if __name__ == "__main__":
	main()
