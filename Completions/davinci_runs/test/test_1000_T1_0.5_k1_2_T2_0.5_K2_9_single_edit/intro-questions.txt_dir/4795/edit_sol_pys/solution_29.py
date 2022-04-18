

import math

def main():
    n = int(input())
    numbers = []
    for i in range(n):
        numbers.append(int(input()))
    total = 0
    for number in numbers:
        length = len(str(number)) # Work out the lengths of the numbers.
        base = int(length / 2)
        power = length - base # Then, work out the power of the number by subtracting the base from the length.
        total += int(math.pow(base, power))
    print(total)

main()
