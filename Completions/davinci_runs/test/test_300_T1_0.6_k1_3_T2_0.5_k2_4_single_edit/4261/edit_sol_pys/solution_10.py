
#
a, b, c = map(int, input().split())

while 1:
    if b + c <= a:
        print(0)
        break
    elif b + c > a:
        print(b + c - a)
        break
