
n = int(input()) 

a = list(map(int, input().split()))

if n < 2:
	print("YES\n0")
	exit(0)

if a[0] > a[1]:
	print("NO")
	exit(0)

for i in range(1, n-1):
	if a[i] < a[i-1] and a[i] > a[i+1]:
		print("NO")
		exit(0)

if a[-1] < a[-2]:
	print("NO")
	exit(0)

print("YES")

for i in range(n):
	if a[i] > a[i-1]:
		print("0 ", end="")
	else:
		print("1 ", end="")
