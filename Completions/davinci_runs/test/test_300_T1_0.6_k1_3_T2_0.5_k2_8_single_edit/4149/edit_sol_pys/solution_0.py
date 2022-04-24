

#Solution

n = int(input())
b = list(map(int, input().split()))[:n]

a = []

for i in range(n):
	if b[i] in b[i + 1:]:
		a.append(b[i])
	else:
		a.append(b[i + 1])

print(*a)
