
# SOLUTION

a, b, c = [int(x) for x in input().split()]

if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a

s = a + c - b
print(s)
