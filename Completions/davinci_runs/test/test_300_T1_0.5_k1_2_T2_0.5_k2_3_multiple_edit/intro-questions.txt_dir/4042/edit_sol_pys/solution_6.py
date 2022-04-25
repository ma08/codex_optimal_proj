

num = input('Enter a number: ')

if num[5] != '5':
    num = num[:5] + '5'

num = float(num)

if num >= 5:
    num = num - 5

num = str(num)
num = num.split('.')

num1 = float(num[0])
num2 = float(num[1])

if num2 >= 50:
    num1 = num1 + 1

if num1 > 10:
    num1 = '10'

print('The number is: ' + str(num1) + '.' + str(num2))
