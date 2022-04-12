

a, b, c = map(int, input().split())
order = input()

if order[0] == 'A':  # A
    if a > b:  # a > b
        a, b = b, a  # a, b = b, a
    if b > c:  # b > c
        b, c = c, b  # b, c = c, b
        if a > b:  # a > b
            a, b = b, a  # a, b = b, a
elif order[0] == 'B':  # B
    if b > a:  # b > a
        b, a = a, b  # b, a = a, b
    if b > c:  # b > c
        b, c = c, b  # b, c = c, b
        if a > b:  # a > b
            a, b = b, a  # a, b = b, a
elif order[0] == 'C':  # C
    if c > a:  # c > a
        c, a = a, c  # c, a = a, c
    if c > b:  # c > b
        c, b = b, c  # c, b = b, c
        if a > b:  # a > b
            a, b = b, a  # a, b = b, a

print(a, b, c)
