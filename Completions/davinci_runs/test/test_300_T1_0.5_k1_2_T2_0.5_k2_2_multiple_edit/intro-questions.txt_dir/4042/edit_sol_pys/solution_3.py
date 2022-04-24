

num = input()

if num[4] != '5':
    num = num[:4] + '5'

num = float(num)

if num >= 3:
    num = num - 3

num = str(num)
num = num.split('.')

num1 = int(num[0])
num2 = int(num[1])

if num2 >= 30:
    num1 = num1 + 1

if num1 > 6:
    num1 = 6

print(num1, num2)
