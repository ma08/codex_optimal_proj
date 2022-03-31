

#------------------------------------------------------------------------------#

def main():
	n, k = [int(i) for i in input().split()]
	a = []
	i = 1
	while n > 0:
		if n < i:
			print("NO")
			return
		a.append(i)
		n -= i
		i += 1
	if len(a) == k:
		print("YES")
		print(" ".join([str(i) for i in a]))
	else:
		print("NO")

main()