

num = input().split(' ')

if num[1][5] != '5':
    num[1] = num[1][:5] + '5'

num[1] = float(num[1])

if num[1] >= 5:
    num[1] = num[1] - 5

num[1] = str(num[1])
num[1] = num[1].split('.')

num1 = int(num[1][0])
num2 = int(num[1][1])

if num2 >= 50:
    num1 = num1 + 1

if num1 > 10:
    num1 = 10

print(num[0], num1, num2)
