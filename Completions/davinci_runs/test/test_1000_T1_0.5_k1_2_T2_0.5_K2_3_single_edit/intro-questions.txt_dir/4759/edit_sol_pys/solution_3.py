

n = int(input())
l = list(map(int, input().split()))

c = 0
s = 0

	if l[i] == -1 and c == 0:
		continue
for i in range(n):
	if l[i] != -1:
		s += l[i]
		c += 1

print(s/c)
