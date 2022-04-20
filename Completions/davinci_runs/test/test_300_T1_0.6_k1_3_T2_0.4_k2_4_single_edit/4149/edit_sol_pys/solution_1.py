

#Solution

n = int(input())
b = list(map(int, input().split()))

a = []

for i in range(n):
	if b[i] in b[n:]: # if b[i] is in the list b[n:]
		a.append(b[i])
	else:
		a.append(b[n + i])

print(*a)
