

n = int(input("Enter the number of elements: "))
a = list(map(int, input("Enter the elements: ").split()))

odds = 0
evens = 0
count = 0

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

print("Number of equal sums of even and odd elements: ", count)
