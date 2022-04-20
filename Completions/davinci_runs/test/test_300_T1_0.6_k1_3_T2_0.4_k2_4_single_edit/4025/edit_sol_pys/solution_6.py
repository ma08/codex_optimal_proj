
a, b, c = map(int, input().split())

if a < b:
    a, b = b, a
if b < c:
    b, c = c, b
if a < b:
    a, b = b, a

days = a + b + c

if a > days // 2:
    days = days // 2
else:
    days = days - a

print(days)
