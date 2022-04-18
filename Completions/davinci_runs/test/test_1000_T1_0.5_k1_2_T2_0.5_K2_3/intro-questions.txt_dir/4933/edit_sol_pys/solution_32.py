

# SOLUTION 2

a, b, c = [int(x) for x in input().split()]  # input

if a > b:  # swap
    a, b = b, a
if b > c:  # swap
    b, c = c, b
if a > b:  # swap
    a, b = b, a

d = a + c - b  # calculate
print(d)  # output
