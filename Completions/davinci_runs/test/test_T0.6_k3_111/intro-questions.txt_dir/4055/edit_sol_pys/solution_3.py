n = int(input())
a = [int(x) for x in input().split()]

x = 0
for i in range(1, n - 1):
    if a[i - 1] == a[i + 1] == 1 and a[i] == 0:
        a[i] = 1
        x += 1

print(x)
