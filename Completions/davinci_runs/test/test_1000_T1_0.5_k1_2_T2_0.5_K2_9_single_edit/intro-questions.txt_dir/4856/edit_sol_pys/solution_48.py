

a, b = input().split()  # input two numbers

if int(a[::-1]) > int(b[::-1]):  # if the first number is greater than the second
    print(a[::-1])
else:
    print(b[::-1])
