

n = int(input())
a = [int(i) for i in input().split()]

a.sort()

count = 1
for i in range(1,n):
    if a[i] != a[i-1]:
        count += 1


print(count)
