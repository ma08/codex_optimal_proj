
a, b, c = map(int, input().split())
order = input().split()

if order[0] == 'A' and order[1] == 'B':
    if a > b:

if order[0] == 'A' and order[1] == 'C':
    if a > c:
        a, c = c, a

if order[0] == 'B' and order[1] == 'A':
    if b > a:
        b, a = a, b

if order[0] == 'B' and order[1] == 'C':
    if b > c:
        b, c = c, b

if order[0] == 'C' and order[1] == 'A':
    if c > a:
        c, a = a, c

if order[0] == 'C' and order[1] == 'B':
    if c > b:
        c, b = b, c

if order[2] == 'A':
        a, b = b, a
    if b > c:
        b, c = c, b
        if a > b:
            a, b = b, a
elif order[2] == 'B':
    if b > a:
        b, a = a, b
    if b > c:
        b, c = c, b
        if a > b:
            a, b = b, a
elif order[2] == 'C':
    if c > a:
        c, a = a, c
    if c > b:
        c, b = b, c
        if a > b:
            a, b = b, a

print(a, b, c)
