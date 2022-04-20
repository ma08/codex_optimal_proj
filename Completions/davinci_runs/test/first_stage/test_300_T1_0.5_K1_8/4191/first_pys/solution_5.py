

a = input()
b = input()
c = input()
d = input()

if a == b and c == d:
    print(1)
elif a == c and b == d:
    print(1)
elif a == d and b == c:
    print(1)
else:
    print(0)