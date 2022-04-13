

import sys

num_participants = int(input())

vaccinated = input().split()
infected = input().split()

efficacy = [0, 0, 0]

for i in range(num_participants):
    if vaccinated[i] == 'Y':
        if infected[i] == 'Y':
            efficacy[0] += 1
        else:
            efficacy[1] += 1
    else:
        if infected[i] == 'Y':
            efficacy[2] += 1

for i in range(3):
    if efficacy[i] > 0:
        print(100 - efficacy[i] / sum(efficacy) * 100)
    else:
        print('Not Effective')
