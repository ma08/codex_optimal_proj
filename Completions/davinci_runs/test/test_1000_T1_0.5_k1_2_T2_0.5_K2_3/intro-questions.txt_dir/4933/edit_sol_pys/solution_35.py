


a, b, c = [int(x) for x in input().split()]  # input as string

if a > b:  # swap if a > b
    a, b = b, a  # swap
if b > c:  # swap if b > c
    b, c = c, b  # swap
if a > b:  # swap if a > b
    a, b = b, a  # swap

d = a + c - b  # find the result
print(d)  # output
