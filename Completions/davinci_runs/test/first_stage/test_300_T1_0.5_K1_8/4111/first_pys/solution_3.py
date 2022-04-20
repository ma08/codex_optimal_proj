

n = int(input())
a = list(map(int, input().split()))

even = 0
odd = 0

for i in range(n):
    if i % 2 == 0:
        even += a[i]
    else:
        odd += a[i]

count = 0

for i in range(n):
    if i % 2 == 0:
        even -= a[i]
    else:
        odd -= a[i]
    if even == odd:
        count += 1
    if i % 2 == 0:
        even += a[i]
    else:
        odd += a[i]

print(count)