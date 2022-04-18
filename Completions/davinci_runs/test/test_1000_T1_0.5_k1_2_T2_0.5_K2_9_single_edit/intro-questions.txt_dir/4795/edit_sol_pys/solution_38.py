

# Work out the lengths of the numbers
# Then, for each number, work out the base of the number by dividing the length by 2
# Then, work out the power of the number by subtracting the base from the length
# Finally, work out the value of the number by taking the base to the power of the power
# Add up all of those values

import math

def main():
    n = int(input()) # number of numbers
    numbers = []
    for i in range(n):
        numbers.append(int(input())) # add each number to list
    total = 0
    for number in numbers: # for each number in the list
        length = len(str(number)) # get the length of the number
        base = int(length / 2) # divide the length by 2 to get the base
        power = length - base # subtract the base from the length to get the power
        total += int(math.pow(base, power)) # add the value to the total
    print(total)

main()
