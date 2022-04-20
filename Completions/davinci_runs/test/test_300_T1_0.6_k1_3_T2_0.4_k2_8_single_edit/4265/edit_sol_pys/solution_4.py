

n = int(input()) # number of elements
s = input() # string s
t = input() # string t

count = 0 # counter
for i in range(n):
	if s[i] != t[i]:
		count += 1

print(count)
