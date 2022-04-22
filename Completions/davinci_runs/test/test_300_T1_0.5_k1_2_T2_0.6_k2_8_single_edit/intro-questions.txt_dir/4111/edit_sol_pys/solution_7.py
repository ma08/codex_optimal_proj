
n = int(input())
a = list(map(int, input().split()))

odds = 0
evens = 0
cnt = 0

for i in range(n):
    if i % 2 == 0:
        evens += a[i]
    else:
        odds += a[i]

for i in range(n):
    if i % 2 == 0:
        evens -= a[i]
    else:
        odds -= a[i]
    if odds == evens:
        cnt += 1
    if i % 2 == 0:
        evens += a[i]
    else:
        odds += a[i]

print(cnt)
