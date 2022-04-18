
#
num = float(input())

if num >= 5:
    num = num - 5

num1 = int(num)
num2 = int((num - num1) * 100)

if num2 >= 50:
    num1 = num1 + 1

if num1 > 9:
    num1 = 9

print(num1, num2)
