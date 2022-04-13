
# CODE:
n = int(input())

side1 = n
side2 = 1

while side1 * side2 != n:
    if side1 * side2 > n:
        side1 -= 1
    else:
        side2 += 1

print(2 * (side1 + side2))
