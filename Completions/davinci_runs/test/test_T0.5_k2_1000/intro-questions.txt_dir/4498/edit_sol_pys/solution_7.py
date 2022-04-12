
a, b, c, d = map(int, input().split())  # input
if d >= abs(a - c):  # if distance is greater than or equal to the distance between a and c
    print('Yes')
elif d >= abs(a - b) and d >= abs(b - c):  # if distance is greater than or equal to the distance between a and b and distance is greater than or equal to the distance between b and c
    print('Yes')
else:
    print('No')
