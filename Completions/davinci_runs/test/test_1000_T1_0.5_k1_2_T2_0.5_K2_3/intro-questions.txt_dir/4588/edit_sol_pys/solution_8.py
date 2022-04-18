
x, y = input().split() #split input string
if int(x, 16) < int(y, 16):
    print("<") #if x is less than y print <
elif int(x, 16) > int(y, 16):
    print(">") #if x is greater than y print >
else:
    print("=") #if x is equal to y print =
