

n = int(input())
a = [int(i) for i in input().split()]

for i in range(n):
    for j in range(n):
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]
print(a)
