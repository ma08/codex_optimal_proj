


# n = int(input())
# s = input()

# n = 6
# s = '(((())'

n = 6
s = '()()()'

# n = 1
# s = ')'

# n = 10
# s = '((((((()'

count = 0
res = 0

for i in s:
	if i == '(':
		count += 1
	else:
		count -= 1
		if count < 0:
			res += 1
			count = 0

print(res)
