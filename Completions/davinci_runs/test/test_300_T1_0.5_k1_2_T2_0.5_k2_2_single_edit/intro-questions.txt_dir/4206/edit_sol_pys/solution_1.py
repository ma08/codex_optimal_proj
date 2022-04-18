
s = input()
digits_divisible_by_3 = 0
for digit in s:
    digits_divisible_by_3 += int(digit) % 3 == 0
digits_remainder_1 = 0
for digit in s:
    digits_remainder_1 += int(digit) % 3 == 1
digits_remainder_2 = 0
for digit in s:
    digits_remainder_2 += int(digit) % 3 == 2
max_cuts = 0
if digits_remainder_1 > digits_divisible_by_3:
    max_cuts += digits_remainder_1 - digits_divisible_by_3
if digits_remainder_2 > digits_divisible_by_3:
    max_cuts += digits_remainder_2 - digits_divisible_by_3
print(max_cuts)
