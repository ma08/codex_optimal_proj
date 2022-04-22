n = int(input())


a = [int(input()) for _ in range(n)]

a.sort()

count = 1
for i in range(1, n):
    if a[i] != a[i-1]:
        count += 1

print(count)
