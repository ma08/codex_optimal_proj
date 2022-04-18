

n = int(input())

a = list(map(int, input().split()))

a.sort()

max_sum = 0
for i in range(n):
    max_sum += a[i]*(n-i)

print(max_sum)
