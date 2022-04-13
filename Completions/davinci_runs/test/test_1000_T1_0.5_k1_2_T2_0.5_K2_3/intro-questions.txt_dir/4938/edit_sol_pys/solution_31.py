

X = int(input())
queue = input()
num_M = 0
num_W = 0
max_people = 0

for person in queue:
    if person == 'M':
        num_M += 1
    else:
        num_W += 1

    if abs(num_M - num_W) > X:
        break
    else:
        max_people += 1

print(max_people)
