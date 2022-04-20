

n, k = map(int, input().split())
a = list(map(int, input().split()))

if k == n:
	print(0)
	exit()

minValue = min(a)
maxValue = max(a)

if maxValue - minValue + 1 < k:
	print(-1)
	exit()

d = {}
for i in a:
	if i in d:
		d[i] += 1
	else:
		d[i] = 1

values = list(d.keys())
values.sort()

if len(values) == 1:
	print(0)
	exit()

if values[0] == values[1]:
	print(0)
	exit()

if values[-1] == values[-2]:
	print(0)
	exit()

count = 0

while True:
	if d[values[0]] >= k:
		break
	else:
		count += 1
		d[values[0]] += 1
		d[values[1]] -= 1
		if d[values[1]] == 0:
			del d[values[1]]
			values.pop(1)

while True:
	if d[values[-1]] >= k:
		break
	else:
		count += 1
		d[values[-1]] += 1
		d[values[-2]] -= 1
		if d[values[-2]] == 0:
			del d[values[-2]]
			values.pop(-2)

print(count)