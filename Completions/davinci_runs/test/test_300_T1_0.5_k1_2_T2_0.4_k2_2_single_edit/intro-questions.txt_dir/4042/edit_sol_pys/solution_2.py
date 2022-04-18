

num = input()

if num[5] != '5':
    num = num[:5] + '5'

num = float(num)

if num >= 5:
    num = num - 5

num = str(num)
num = num.split('.')

num1 = int(num[0])
num2 = int(num[1])

if num2 >= 50:
    num1 = num1 + 1

if num1 > 10:
    num1 = 9

print(num1, num2)
