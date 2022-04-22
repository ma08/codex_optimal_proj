

num = input()  # input number

if num[5] != '5':  # if the number is not 5, add 5 to the end of the number
    num = num[:5] + '5'

num = float(num)  # convert to float

if num >= 5:  # if the number is greater than or equal to 5
    num = num - 5

num = str(num)  # convert to string
num = num.split('.')  # split the number

num1 = int(num[0])  # first number
num2 = int(num[1])  # second number

if num2 >= 50:  # if the second number is greater than or equal to 50
    num1 = num1 + 1

if num1 > 10:  # if the first number is greater than 10
    num1 = 10

print(num1, num2)

