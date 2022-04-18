
a, b, c = map(int, input().split()) # input the three numbers
order = input() # input the order of the numbers (A, B, or C)

if order[0] == 'A': # if the first number is A
    if a > b:
        a, b = b, a
    if b > c:
        b, c = c, b
        if a > b:
            a, b = b, a
elif order[0] == 'B': # if the first number is B
    if b > a:
        b, a = a, b
    if b > c:
        b, c = c, b
        if a > b:
            a, b = b, a
elif order[0] == 'C': # if the first number is C
    if c > a:
        c, a = a, c
    if c > b:
        c, b = b, c
        if a > b:
            a, b = b, a

print(a, b, c)
