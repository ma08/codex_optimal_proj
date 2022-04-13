

x, y = input().split() #split the input into 2 string

if int(x, 16) < int(y, 16): #compare the input
    print("<")
elif int(x, 16) > int(y, 16):
    print(">")
else:
    print("=")
