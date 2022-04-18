
# Read in the length of the sequence
# Read in the numbers
# For each number, if it's the same as the previous, add one to the current streak
# If it's not the same, add the current streak to the total streak
# Then, set the current streak to 1
# Finally, print the total streak

import math

def main():
    length = int(input())
    numbers = [int(input()) for i in range(length)]
    currentStreak = 1
    totalStreak = 0
    for i in range(length):
        if i == length-1:
            break
        if numbers[i] == numbers[i+1]:
            currentStreak += 1
        else:
            totalStreak += currentStreak
            currentStreak = 1
    print(totalStreak)

main()
