

n = int(input())
a = list(map(int, input().split()))

total_sum = sum(a)

s = set()
for i in range(n):
	if total_sum - a[i] == a[i]:
		s.add(i+1)

print(len(s) if len(s) != 0 else -1)
print(*s if len(s) != 0 else -1)
