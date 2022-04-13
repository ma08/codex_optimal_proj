N = int(input())  # number of test cases
output = 0  # output
for i in range(N):  # loop through test cases
    power = 0  # power of each number
    number = input()  # the number
    for i in range(len(number)):  # loop through each digit in number
        power += int(number[i])  # add each digit to the power
    output += power ** len(number)  # add the number to the output
print(output)  # print the output
