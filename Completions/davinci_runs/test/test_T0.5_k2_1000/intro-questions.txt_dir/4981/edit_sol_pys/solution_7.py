
a, b, c = map(int, input().split())  # input
order = input()

if order[0] == 'A':
    if a > b:
        a, b = b, a
    if b > c:
        b, c = c, b
        if a > b:
            a, b = b, a
elif order[0] == 'B':
    if b > a:
        b, a = a, b
    if b > c:
        b, c = c, b
        if a > b:
            a, b = b, a
elif order[0] == 'C':
    if c > a:
        c, a = a, c
    if c > b:
        c, b = b, c
        if a > b:
            a, b = b, a

print(a, b, c)
