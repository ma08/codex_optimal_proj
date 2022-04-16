

x, y = input().split()  # input is separated by space

if int(x, 16) < int(y, 16):
    print("<")
elif int(x, 16) > int(y, 16):
    print(">")
else:
    print("=")
