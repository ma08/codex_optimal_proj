

num = int(input())  # input number

while num > 9:  # while number is bigger than 9
    num = str(num)
    num = [int(i) for i in num]  # convert to list
    num = [i for i in num if i != 0]  # remove 0
    num = [str(i) for i in num]
    num = ''.join(num)
    num = int(num)

print(num)
