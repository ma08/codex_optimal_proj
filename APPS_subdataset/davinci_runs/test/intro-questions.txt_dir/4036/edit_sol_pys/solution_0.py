

#------------------------------------------------------------------------------#

def main():
	n, k = [int(i) for i in input().split()] # n = number of stones, k = number of piles
	a = []
	i = 1
	while n > 0:
		if n < i: # if this condition is met, the number of stones is less than the number of piles
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
