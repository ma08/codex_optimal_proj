

# CODE:
n = int(input()) #number of tiles

side1 = n #first side
side2 = 1 #second side

while side1 * side2 != n:
    if side1 * side2 > n:
        side1 -= 1
    else:
        side2 += 1

print(2 * (side1 + side2)) #perimeter
