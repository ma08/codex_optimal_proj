x = int(input())
genders = input().split()

women = 0
men = 0
total = 0

for gender in genders[:x]:
    if gender == 'W':
        women += 1
    else:
        men += 1
    if abs(men - women) <= x - 1:
        total += 1
    else:
        break

print(total)
