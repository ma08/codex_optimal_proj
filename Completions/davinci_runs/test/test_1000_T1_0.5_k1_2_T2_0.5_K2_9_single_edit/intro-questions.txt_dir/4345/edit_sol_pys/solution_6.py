

n = int(input())

a = list(map(int, input().split()))

if n < 2:
	print("YES\n0", end="")
	exit()

if a[0] > a[1]:
	print("NO", end="")
	exit()

for i in range(1, n-1):
	if a[i] < a[i-1] and a[i] > a[i+1]:
		print("NO", end="")
		exit()

if a[-1] < a[-2]:
	print("NO", end="")
	exit()

print("YES", end="")

for i in range(n):
	if a[i] > a[i-1]:
		print("\n0", end="")
	else:
		print("\n1", end="")
