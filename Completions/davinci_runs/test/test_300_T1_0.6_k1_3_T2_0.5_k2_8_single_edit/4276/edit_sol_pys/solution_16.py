#

n, t = map(int, input().split())

c = []
for i in range(n):
	c.append(list(map(int, input().split())))

c.sort(key=lambda x:x[0])
for i in c:
	if i[1] <= t:
		print(i[0])
		exit()
print("TLE")
