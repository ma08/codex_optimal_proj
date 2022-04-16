

# Work out the lengths of the numbers. Then, for each number, work out the base of the number by dividing the length by 2. Then, work out the power of the number by subtracting the base from the length. Finally, work out the value of the number by taking the base to the power of the power. Add up all of those values.

import math

def main():
    n = int(input()) # number of numbers
    numbers = [] # list of numbers
    for i in range(n): # for each number
        numbers.append(int(input())) # add it to the list
    total = 0 # the total
    for number in numbers: # for each number in the list
        length = len(str(number)) # length of the number
        base = int(length / 2) # base of the number
        power = length - base # power of the number
        total += int(math.pow(base, power)) # add the value of the number to the total
    print(total) # print the total

main()
