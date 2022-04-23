

num = input()  # input number

if num[5] != '5':  # if number is not multiple of 5
    num = num[:5] + '5'  # add 5 to number

num = float(num)  # convert number to float

if num >= 5:  # if number is greater than 5
    num = num - 5  # subtract 5 from number

num = str(num)  # convert number to string
num = num.split('.')  # split number into two parts

num1 = int(num[0])  # first part of number
num2 = int(num[1])  # second part of number

if num2 >= 50:  # if second part of number is greater than 50
    num1 = num1 + 1  # add 1 to first part of number

if num1 > 10:  # if first part of number is greater than 10
    num1 = 10  # first part of number is 10

print(num1, num2)  # print number
