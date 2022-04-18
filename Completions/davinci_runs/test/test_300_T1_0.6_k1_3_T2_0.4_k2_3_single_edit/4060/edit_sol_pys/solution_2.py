


n = int(input())
s = input()

# n = 6
# s = '(((())'

# # n = 6
# # s = '()()()'

# # n = 1
# # s = ')'

# # n = 8
# # s = ')))(((((('

count_open = 0
count_close = 0
res = 0

for i in s:
	if i == '(':
		count_open += 1
	else:
		count_close += 1
		if count_close > count_open:
			res += 1
			count_open, count_close = count_close, count_open

print(res)
