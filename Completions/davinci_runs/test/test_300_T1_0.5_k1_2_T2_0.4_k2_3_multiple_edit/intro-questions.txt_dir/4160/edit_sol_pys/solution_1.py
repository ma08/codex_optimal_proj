

n = int(input())
a = [int(x) for x in input().split()]
i = 0
while i < n - 1:
    if a[i] > a[i + 1]:
        print(i + 1)
        break
    i += 1
else:
    print(0)
