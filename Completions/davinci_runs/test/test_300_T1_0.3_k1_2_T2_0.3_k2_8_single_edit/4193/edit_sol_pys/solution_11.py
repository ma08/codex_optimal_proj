

import sys

# Read numbers as a list of strings
numbers = sys.stdin.read().split()

# Convert list of strings to list of numbers
numbers = list(map(int, numbers))

# Populate the bingo sheet
bingo_sheet = [[numbers[0], numbers[1], numbers[2]],
               [numbers[3], numbers[4], numbers[5]],
               [numbers[6], numbers[7], numbers[8]]]

# Get the number of numbers to be chosen
num_numbers_to_choose = numbers[9]

# Get the numbers to be chosen
numbers_to_choose = numbers[10:]

# Check if the bingo sheet contains any of the numbers to be chosen
for number in numbers_to_choose:
    for i in range(3):
        for j in range(3):
            if number == bingo_sheet[i][j]:
                bingo_sheet[i][j] = 0

# Check if there are three numbers in a row, column, or diagonal
bingo = False

# Check rows
for i in range(3):
    if bingo_sheet[i][0] == 0 and bingo_sheet[i][1] == 0 and bingo_sheet[i][2] == 0:
        bingo = True
        break

# Check columns
for j in range(3):
    if bingo_sheet[0][j] == 0 and bingo_sheet[1][j] == 0 and bingo_sheet[2][j] == 0:
        bingo = True
        break

# Check diagonals
if bingo_sheet[0][0] == 0 and bingo_sheet[1][1] == 0 and bingo_sheet[2][2] == 0:
    bingo = True
elif bingo_sheet[0][2] == 0 and bingo_sheet[1][1] == 0 and bingo_sheet[2][0] == 0:
    bingo = True

# Print result
if bingo:
    print('Yes')
else:
    print('No')
