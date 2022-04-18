x = int(input())
genders = input().split()

women = 0
men = 0
total = 0

for i in range(len(genders)):
	if genders[i] == 'W':
		women += 1
	else:
		men += 1
	if abs(men - women) <= x:
		total += 1
	elif abs(men - women) > x:
		break

print(total + 1)
