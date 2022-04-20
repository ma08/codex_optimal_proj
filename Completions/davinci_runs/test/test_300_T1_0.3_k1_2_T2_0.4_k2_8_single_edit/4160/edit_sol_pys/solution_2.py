

n = int(input())

a = [int(i) for i in input().split()]

m = int(input())

b = [int(i) for i in input().split()]

a.sort()
b.sort()

i = 0
j = 0

while i < n and j < m:
    if abs(a[i] - b[j]) <= 1:
        i += 1
        j += 1
    elif a[i] > b[j]:
        j += 1
    else:
        i += 1

print(i + j)
