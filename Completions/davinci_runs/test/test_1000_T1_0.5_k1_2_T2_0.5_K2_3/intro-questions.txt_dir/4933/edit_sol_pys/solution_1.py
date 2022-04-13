

# SOLUTION

a, b, c = [int(x) for x in raw_input().split()]

if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a

d = a + c - b
print(d)
