
n = int(input()) #input

a = list(map(int, input().split())) #input

if n < 2: #edge case
	print("YES\n0")
	exit()

if a[0] > a[1]: #first element check
	print("NO")
	exit()

for i in range(1, n-1): #check the middle elements
	if a[i] < a[i-1] and a[i] > a[i+1]:
		print("NO")
		exit()

if a[-1] < a[-2]: #last element check
	print("NO")
	exit()

print("YES") #print YES

for i in range(n): #print the answer
	if a[i] > a[i-1]:
		print("0 ", end="")
	else:
		print("1 ", end="")
