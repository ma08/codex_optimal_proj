
n = int(input())
l = list(map(int, input().split()))

count = 0
sum = 0

for i in range(n):
	if l[i] != -1:
		sum += l[i]
		count += 1

print(sum/count)
