

# main

x = int(input())

# 500 yen
five_hundred = x // 500
x = x % 500

# 100 yen
one_hundred = x // 100
x = x % 100

# 50 yen
fifty = x // 50
x = x % 50

# 10 yen
ten = x // 10
x = x % 10

# 5 yen
five = x // 5
x = x % 5

# 1 yen
one = x // 1
x = x % 1

print(five_hundred * 1000 + one_hundred * 100 + fifty * 50 + ten * 10 + five * 5 + one * 1)