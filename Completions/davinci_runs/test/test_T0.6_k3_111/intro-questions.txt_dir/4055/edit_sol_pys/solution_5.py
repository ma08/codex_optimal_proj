n = int(input())
a = [int(x) for x in input().split(' ')]

count = 0
for i in range(1, n - 1):
    if a[i - 1] == 1 and a[i + 1] == 1 and a[i] == 0:
        count += 1

print(count)
