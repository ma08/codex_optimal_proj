
def main():
	n, k = map(int, input().split())
	a = list(map(int, input().split()))
	s = set()
	for x in a:
		if x in s:
			s.remove(x)
		else:
			s.add(x)
			if len(s) > k:
				print("NO")
				return
	if len(s) < k:
		print("NO")
		return
	print("YES")
	d = {}
	for i in range(1, k+1):
		d[i] = set()
	for i in range(1, n+1):
		for j in range(1, k+1):
			if i not in d[j]:
				d[j].add(i)
				print(j, end=" ")
				break

main()