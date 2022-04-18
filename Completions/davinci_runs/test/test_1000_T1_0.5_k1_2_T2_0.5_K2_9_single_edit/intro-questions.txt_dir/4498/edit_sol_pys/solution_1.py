

a, b, c, d = [int(i) for i in input().split()]
if d >= abs(a - c):
    print('Yes')
elif d >= abs(a - b) and d >= abs(b - c):
    print('Yes')
else:
    print('No')
