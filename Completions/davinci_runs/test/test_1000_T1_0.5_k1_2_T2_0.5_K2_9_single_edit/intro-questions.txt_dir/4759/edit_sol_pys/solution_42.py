

n = int(input())
l = list(map(int, input().split()))

c = 0
v = 0
s = 0

for i in range(n):
	if l[i] != -1:
		s += l[i]
	else:
		v += 1
		c += 1

print((s+v)/(c+v))
