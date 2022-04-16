

x = int(input()) # maximum difference of number of women and men
genders = input() # string of 'W' and 'M'

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
