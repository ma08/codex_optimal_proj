

def main():
	n,h,l,r = map(int,input().split())
	a = list(map(int,input().split()))
	curr = 0
	count = 0
	for i in range(n):
		curr += a[i]-1
		if curr >= h:
			curr -= h
		if curr >= l and curr <= r:
			count += 1
		curr += 1
	print(count)

if __name__ == "__main__":
	main()