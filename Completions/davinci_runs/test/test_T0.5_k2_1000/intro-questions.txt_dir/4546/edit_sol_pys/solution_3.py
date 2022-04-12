

a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a == b == c == d:
    print(6)
elif a == b == c or a == b == d or a == c == d or b == c == d:
    print(3)
elif a == b or a == c or a == d or b == c or b == d or c == d:
    print(2)
else: print(0)
