
x, y = input().split()   # split the input by space

if int(x, 16) < int(y, 16):
    print("<")
elif int(x, 16) > int(y, 16):
    print(">")
else:
    print("=")
