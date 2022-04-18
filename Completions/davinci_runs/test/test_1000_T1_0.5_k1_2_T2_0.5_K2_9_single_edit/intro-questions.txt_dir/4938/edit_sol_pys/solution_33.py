

x = int(input('enter a number: '))
genders = input('enter a string: ')

women = 0
men = 0
total = 0

for gender in genders:
    if gender == 'W':
        women += 1
    else:
        men += 1
    if abs(men - women) <= x and men + women == len(genders):
        total += 1
    else:
        break

print(total)
