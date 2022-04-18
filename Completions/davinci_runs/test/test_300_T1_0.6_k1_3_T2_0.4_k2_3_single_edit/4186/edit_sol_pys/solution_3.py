n = int(input())
a = list(map(int, input().split()))

b = []
for i in range(n):
    b.append(a[i] + a[i-1])

print(b)
