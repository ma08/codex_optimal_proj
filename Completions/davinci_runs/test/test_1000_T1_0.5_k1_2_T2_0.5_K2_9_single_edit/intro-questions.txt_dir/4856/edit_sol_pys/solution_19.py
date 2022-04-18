

a, b = input().split()  # taking input from user

if int(a[::-1]) > int(b[::-1]):  # reversing the number and comparing
    print(a[::-1])
else:
    print(b[::-1])
