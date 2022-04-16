
#Problem: https://www.hackerrank.com/challenges/reduced-string/problem
#-----Solution-----
n, k = [int(x) for x in input().split(" ")]

for i in range(k):
	if n%10 == 0:
		n = n//10
	else:
		n = n-1

print(n)
