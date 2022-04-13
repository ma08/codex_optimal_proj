

numbers = input().split()  # input numbers

for i in range(5):  # loop
    if numbers[i] == "0":  # check if the number is zero
        print(i+1)  # print the position
