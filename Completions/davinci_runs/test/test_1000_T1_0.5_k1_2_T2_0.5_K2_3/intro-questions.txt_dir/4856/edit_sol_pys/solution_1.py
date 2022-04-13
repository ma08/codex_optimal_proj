
#-----main-----#
a, b = input().split()  # input two numbers and split them

if int(a[::-1]) > int(b[::-1]):  # compare two numbers in reverse order
    print(a[::-1])  # if a > b, print a
else:
    print(b[::-1])  # else, print b
