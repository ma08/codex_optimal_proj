
# get input
num1, num2 = map(int, input().split()) # this line can be written as num1, num2 = [int(x) for x in input().split()]

# calculate sum and output
if num1 + num2 >= 10:
    print("error")
else:
    print(num1 + num2)
