

x, y = input().split() #split the input into x, y

if int(x, 16) < int(y, 16): #compare the input and print the result
    print("<")
elif int(x, 16) > int(y, 16):
    print(">")
else:
    print("=")
