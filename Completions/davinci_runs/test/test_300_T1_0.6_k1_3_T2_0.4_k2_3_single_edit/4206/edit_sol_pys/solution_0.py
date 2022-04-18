

input = input("Enter a number: ")

if len(input) == 1:
    print("There is 1 way to split this number.")
else:
    count = 0
    for i in range(1, len(input)):
        if int(input[:i]) % 3 == 0:
            count += 1
    print("There are {} ways to split this number.".format(count))
