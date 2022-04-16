
x = int(input('enter number of seats'))
genders = input('enter gender')
women = 0
men = 0
total = 0

for gender in genders:
    if gender == 'W':
        women += 1
    else:
        men += 1
    if abs(men - women) <= x:
        total += 1
    else:
        break

print(total)
