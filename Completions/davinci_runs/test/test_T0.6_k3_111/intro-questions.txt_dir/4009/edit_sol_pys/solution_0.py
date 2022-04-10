
n, x, y = map(int, input().split())
number = input()

number = list(number)

for i in range(n-y, n+1):
	if number[i] == '0':
		number[i] = '1'
	else:
		number[i] = '0'

print(n-x-y+1)
