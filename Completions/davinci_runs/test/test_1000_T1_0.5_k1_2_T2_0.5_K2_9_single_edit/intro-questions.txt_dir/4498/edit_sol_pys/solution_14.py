'''
x = int(input())
y = int(input())
if x > 0 and y > 0:
    print('1')
elif x < 0 and y > 0:
    print('2')
elif x < 0 and y < 0:
    print('3')
elif x > 0 and y < 0:
    print('4')
'''

a, b, c, d = map(int, input().split())
if d >= abs(a - c):
    print('Yes')
elif d >= abs(a - b) and d >= abs(b - c):
    print('Yes')
else:
    print('No')
