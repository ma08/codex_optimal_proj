

n = int(input())
a = list(map(int, input().split()))

odds = 0
evens = 0
count = 0

for i in range(n):
    if i % 2 == 0:
        evens += a[i]
    else:
        odds += a[i]

for i in range(n):
    if i != 0:
        if i % 2 == 0:
            evens -= a[i-1]
        else:
            odds -= a[i-1]
        if odds == evens:
            count += 1
        if i % 2 == 0:
            evens += a[i-1]
        else:
            odds += a[i-1]

print(count)
