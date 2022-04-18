
X = int(input())
line = input()

women = men = 0

for person in line:
    if person == 'W':
        women += 1
        if women > X:
            break
    elif person == 'M':
        men += 1 
        if men > X:
            break

print(women + men)
