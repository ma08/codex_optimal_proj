

# Given a number, work out the length of the number
# Then, for each digit in the number, work out the base of the digit by dividing the length by 2
# Then, work out the power of the digit by subtracting the base from the length
# Finally, work out the value of the digit by taking the base to the power of the power
# Add up all of the values

import math

def main():
    n = int(input())
    numbers = []
    for i in range(n):
        numbers.append(int(input()))
    total = 0
    for number in numbers:
        length = len(str(number))
        base = int(length / 2)
        power = length - base
        total += int(math.pow(base, power))
    print(total)

main()
