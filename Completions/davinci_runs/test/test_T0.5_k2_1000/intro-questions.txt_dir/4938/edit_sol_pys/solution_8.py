
x = int(input())  # number of days
s = input()  # string of W and M

w = 0  # number of W
m = 0  # number of M
i = 0  # number of days

for c in s:
    if c == 'W':
        w += 1
    else:
        m += 1
    if abs(w - m) > x:
        break
    i += 1

print(i)
