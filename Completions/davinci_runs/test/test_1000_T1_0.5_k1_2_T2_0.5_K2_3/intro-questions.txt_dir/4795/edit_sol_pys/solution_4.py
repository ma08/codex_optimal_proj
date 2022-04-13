

# For each number, work out the base of the number by dividing the length by 2 (integer division).
# Then, work out the exponent of the number by subtracting the base from the length and adding 1.
# Finally, work out the value of the number by taking the base to the power of the exponent and adding 1.
# Add up all of the values and print the total.

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
        power = length - base + 1
        total += int(math.pow(base, power))
    print(total)

main()
