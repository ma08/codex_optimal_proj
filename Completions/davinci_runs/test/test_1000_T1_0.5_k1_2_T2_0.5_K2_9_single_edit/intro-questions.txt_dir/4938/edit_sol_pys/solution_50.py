

X = input()
line = input()

women = men = 0

for person in line:
    if person == 'W':
        women += 1
    else:
        men += 1

    if abs(women - men) > int(X):
        break

print(women + men)
