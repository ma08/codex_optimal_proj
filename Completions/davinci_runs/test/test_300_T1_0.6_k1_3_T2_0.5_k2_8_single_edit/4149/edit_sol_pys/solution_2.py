
#Solution

n = int(input()) #num of elements
b = list(map(int, input().split())) #list of elements

a = [] #new list

for i in range(n):
	if b[i] in b[n:]: #if b[i] is in the second half of the list
		a.append(b[i])
	else:
		a.append(b[n + i]) #if b[i] is in the first half of the list

print(*a)
