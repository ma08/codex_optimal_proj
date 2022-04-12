

x, y = input().split()  # split the input into two variables 

if int(x, 16) < int(y, 16):  # check if the first variable is smaller than the second
    print('<')
elif int(x, 16) > int(y, 16):
    print('>')
else:
    print('=')
