
n = int(input())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

if a[0] > b[1]:  # Assume the first player attacks the second player
    a[0] -= b[1]
    b[1] = 0
else:
    b[1] -= a[0]
    a[0] = 0
if a[2] > b[0]:  # Assume the first player attacks the third player
    a[2] -= b[0]
    b[0] = 0
else:
    b[0] -= a[2]
    a[2] = 0
if a[1] > b[2]:  # Assume the second player attacks the third player
    a[1] -= b[2]
    b[2] = 0
else:
    b[2] -= a[1]
    a[1] = 0

print(min(a), max(a))
