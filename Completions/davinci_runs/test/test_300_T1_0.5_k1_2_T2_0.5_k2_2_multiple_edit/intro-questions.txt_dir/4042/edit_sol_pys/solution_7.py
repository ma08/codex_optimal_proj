

num = input()  # input num

# if num[5] != '5':
#     num = num[:5] + '5'

if num[5] != '5':  # if num[5] not equal 5
    num = num[:5] + '5'

num = float(num)  # string to float

if num >= 5:  # if num greater or equal 5
    num = num - 5

num = str(num)  # float to str
num = num.split('.')  # string to list

num1 = int(num[0])  # string to int
num2 = int(num[1])  # string to int

if num2 >= 50:  # if num2 greater or equal 50
    num1 = num1 + 1

if num1 > 10:  # if num1 greater 10
    num1 = 10

print(num1, num2)  # output num
