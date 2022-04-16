

# Work out the length of the numbers.
# Then, for each number, work out the base of the number by dividing the length by 2 and rounding down.
# Then, work out the power of the number by subtracting the base from the length and rounding up.
# Finally, work out the value of the number by taking the base to the power of the power and rounding up.
# Add up all of those values and print the result.

import math

def main():
    n = int(input())
    numbers = []
    for i in range(n):
        numbers.append(int(input()))
    total = 0
    for number in numbers:
        length = len(str(number))
        base = math.floor(length / 2)
        power = math.ceil(length - base)
        total += math.ceil(math.pow(base, power))
    print(total)

main()
