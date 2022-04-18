

X = int(input())
queue = input()
num_men = 0
num_women = 0
max_people = 0

for person in queue:
    if person == 'M':
        num_men += 1
    else:
        num_women += 1

    if abs(num_men - num_women) > X:
        break
    else:
        max_people += 1

print(max_people)
