

x, y = input().split()  #split the input

if int(x, 16) < int(y, 16):  #compare the input
    print("<")
elif int(x, 16) > int(y, 16):
    print(">")
else:
    print("=")
