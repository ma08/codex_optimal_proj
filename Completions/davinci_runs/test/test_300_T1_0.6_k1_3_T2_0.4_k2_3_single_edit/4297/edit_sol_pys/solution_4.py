

#input 2 integers
a, b = [int(x) for x in input().split()]

#if a is less than b, print a
if a < b:
    print(a)

#if a is greater than b, print b
elif a > b:
    print(b)

#if a is equal to b, print a and b
else:
    print(a)
    print(b)
