n = int(input())
a = list(map(int, input().split()))


odd = 0
even = 0
for i in range(n):
    if i % 2 == 0:
        odd += a[i]
    else:
        even += a[i]

print(odd)
print(even)
