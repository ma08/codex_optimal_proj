

import math

def main():
    n = int(input()) # The number of numbers to be input.
    numbers = []
    for i in range(n):
        numbers.append(int(input())) # The numbers themselves.
    total = 0
    for number in numbers:
        length = len(str(number)) # Work out the length of the number.
        base = int(length / 2) # Work out the base of the number.
        power = length - base # Work out the power of the number.
        total += int(math.pow(base, power))
    print(total)

main()
