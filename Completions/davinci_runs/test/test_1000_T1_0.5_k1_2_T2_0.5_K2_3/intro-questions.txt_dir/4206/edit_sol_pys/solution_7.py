
s = str(s)
s = input()

# Count the number of digits that are divisible by 3.
digits_divisible_by_3 = 0
for digit in s:
    if int(digit) % 3 == 0:
        digits_divisible_by_3 += 1

# Count the number of digits that have a remainder of 1.
digits_remainder_1 = 0
for digit in s:
    if int(digit) % 3 == 1:
        digits_remainder_1 += 1

# Count the number of digits that have a remainder of 2.
digits_remainder_2 = 0
for digit in s:
    if int(digit) % 3 == 2:
        digits_remainder_2 += 1

# Compute the maximum number of cuts that can be made.
max_cuts = 0

# We can always cut a digit that is divisible by 3.
max_cuts += digits_divisible_by_3

# We can cut a digit that is not divisible by 3 if the number of digits
# with the same remainder is greater than the number of digits that are
# divisible by 3.
if digits_remainder_1 > digits_divisible_by_3:
    max_cuts += digits_remainder_1 - digits_divisible_by_3

if digits_remainder_2 > digits_divisible_by_3:
    max_cuts += digits_remainder_2 - digits_divisible_by_3

print(max_cuts)
