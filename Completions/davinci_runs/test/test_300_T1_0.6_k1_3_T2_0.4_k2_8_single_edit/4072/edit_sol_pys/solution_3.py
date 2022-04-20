

a = int(input()) # input a number

if a < 100: # if a is less than 100
    print(0)
elif a % 10 != 0: # if a is not divisible by 10
    print(1)
else: # if a is divisible by 10
    print(0)
