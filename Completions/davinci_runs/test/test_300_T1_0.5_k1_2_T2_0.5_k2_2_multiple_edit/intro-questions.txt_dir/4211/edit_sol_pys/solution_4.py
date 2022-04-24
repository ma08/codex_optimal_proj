
n = int(input())
a = list(map(int, input().split()))

b = []

for i in range(n-1):
    if a[i] <= a[i+1]:
        b.append(a[i])
    else:
        b.append(a[i+1])

b.append(a[n-1])

print(sum(b))
