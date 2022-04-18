

n = int(input())  # Number of test cases
a = list(map(int, input().split()))  # Input array

odds = 0  # Sum of odd elements
evens = 0  # Sum of even elements
count = 0  # Number of subarrays

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
