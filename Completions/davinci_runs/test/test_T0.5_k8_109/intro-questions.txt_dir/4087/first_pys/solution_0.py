

# Function to check if the number is divisible by 4
def divisibleByFour(num):
    sum = 0
    for i in str(num):
        sum += int(i)
    if sum % 4 == 0:
        return True
    return False

# Function to find the next number divisible by 4
def nextDivisibleByFour(num):
    while divisibleByFour(num) == False:
        num += 1
    return num

print(nextDivisibleByFour(int(input())))