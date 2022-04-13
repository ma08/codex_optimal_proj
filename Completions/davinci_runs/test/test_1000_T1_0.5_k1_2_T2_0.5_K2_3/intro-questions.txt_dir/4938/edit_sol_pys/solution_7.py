

x = int(input())  # the number of people to be invited 
genders = input()  # the genders of the people 

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
