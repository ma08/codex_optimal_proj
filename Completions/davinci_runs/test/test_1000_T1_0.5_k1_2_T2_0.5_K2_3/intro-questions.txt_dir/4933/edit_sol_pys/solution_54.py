

from sys import stdin

numbers = [int(x) for x in stdin.readline().split()]
numbers.sort()
missing = 0
if numbers[1] - numbers[0] != numbers[2] - numbers[1]:
	missing = numbers[2] + numbers[1] - numbers[0]
else:
	missing = numbers[2] + numbers[2] - numbers[1]

print(missing)
