

x, y = input().split()

if int(x, 16) < int(y, 16):
    print('<')
elif int(x, 16) > int(y, 16):
    print('>')
else:
    print('=')