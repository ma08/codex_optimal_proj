

n = int(input())  # number of elements in array
a = list(map(int, input().split()))  # input array

odds = 0  # sum of odds numbers
evens = 0  # sum of evens numbers
count = 0  # counter for number of equal sums of odds and evens

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
        count += 1
    if i % 2 == 0:
        evens += a[i]
    else:
        odds += a[i]

print(count)
