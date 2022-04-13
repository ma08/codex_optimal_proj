import math

# Work out the lengths of the numbers
# Then, for each number, work out the base of the number by dividing the length by 2
# Then, work out the power of the number by subtracting the base from the length
# Finally, work out the value of the number by taking the base to the power of the power
# Add up all of those values

def main():
    n = int(input(""))
    numbers = []
    for i in range(n):
        numbers.append(int(input("")))
    total = 0
    for number in numbers:
        length = len(str(number))
        base = int(length / 2)
        power = length - base
        total += int(math.pow(base, power))
    print(total)

main()
