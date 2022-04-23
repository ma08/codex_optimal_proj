

num = input()  # input a number

if num[5] != '5':  # if number is not 5
    num = num[:5] + '5'  # add 5 to number

num = num[:5] + '5'  # add 5 to number
num = float(num)  # convert number to float

if num >= 5:  # if number is greater than 5
    num = num - 5  # subtract 5 from number

num = str(num)  # convert number to string
num = num.split('.')  # split number by decimal point

num1 = int(num[0])  # convert number before decimal point to integer
num2 = int(num[1])  # convert number after decimal point to integer

if num2 >= 50:  # if number after decimal point is greater than 50
    num1 = num1 + 1  # add 1 to number before decimal point

if num1 > 10:  # if number before decimal point is greater than 10
    num1 = 10  # make number before decimal point 10

print(num1, num2)  # print number before and after decimal point
