

x = int(input())
genders = input()

women, men, total = 0, 0, 0

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
