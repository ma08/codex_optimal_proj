

# Solution

n = int(input())
b = list(map(int, input().split()))

a = []

for i in range(len(b)):
	if b[i] in a:
		a.append(b[i])
	elif b[i] in b[i+1:]:
		a.append(b[i])
	else:
		a.append(b[i])

print(*a[:n])