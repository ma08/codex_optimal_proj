

def main():
	n, k = [int(x) for x in input().split()]
	if n < k or n > 10**9 or k > 10**5:
		print("NO")
		return
	if n == k:
		print("YES")
		print(" ".join([str(x) for x in range(1, k+1)]))
		return
	if n % 2 == 0:
		if k == 2:
			print("YES")
			print("{} {}".format(n//2, n//2))
			return
		if k == 3:
			print("YES")
			print("{} 1 {}".format(n//2, n//2-1))
			return
		if k == 4:
			print("YES")
			print("2 1 3 3")
			return
		if k == 5:
			print("YES")
			print("2 1 2 3 3")
			return
		if k == 6:
			print("YES")
			print("2 1 2 2 3 3")
			return
		if k > 6:
			print("NO")
			return
	if n % 2 == 1:
		if k == 2:
			print("YES")
			print("{} {}".format(n//2 + 1, n//2))
			return
		if k == 3:
			print("YES")
			print("{} 1 {}".format(n//2+1, n//2-1))
			return
		if k == 4:
			print("YES")
			print("2 1 3 3")
			return
		if k == 5:
			print("YES")
			print("2 1 2 3 3")
			return
		if k == 6:
			print("YES")
			print("2 1 2 2 3 3")
			return
		if k > 6:
			print("NO")
			return

if __name__ == '__main__':
	main()
