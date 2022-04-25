

x = [int(i) for i in input().split()]  # list comprehension
if x[0] < x[1]:
    print('<')
elif x[0] == x[1]:
    print('=')
else:
    print('>')
