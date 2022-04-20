

num = float(input())

num = str(num)
num = num.split('.')
num1 = int(num[0])
num2 = int(num[1])

if num2 >= 50:
    num1 = num1 + 1

if num1 > 10:
    num1 = 10

num1 = str(num1)
num2 = str(num2)

num = num1 + num2
num = float(num)

if num >= 5:
    num = num - 5

print(num)
