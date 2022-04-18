# coding=utf-8

x = int(input('x = '))
y = int(input('y = '))

i = 1
while i <= x and i <= y:
    if x % i == 0 and y % i == 0:
        d = i
    i += 1
print('НОД =', d)
