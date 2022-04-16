

x, y = input().split()  # split the input

if int(x, 16) < int(y, 16):  # if x is smaller than y
    print('<')
elif int(x, 16) > int(y, 16):  # if x is greater than y
    print('>')
else:
    print('=')  # if x is equal to y
