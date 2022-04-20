
def main():
	n = int(input())
	a = list(map(int, input().split()))
	min_a = min(a)
	max_a = max(a)
	if min_a == max_a:
		print("YES")
	else:
		print("NO")

if __name__ == "__main__":
	main()
