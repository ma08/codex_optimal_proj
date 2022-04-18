

#SOLUTION

a, b, c = [float(x) for x in input().split()]

if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a

d = a + b - c
print(d)
