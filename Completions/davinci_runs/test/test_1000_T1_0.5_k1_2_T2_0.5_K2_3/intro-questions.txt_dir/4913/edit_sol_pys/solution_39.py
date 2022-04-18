
import sys

vaccinated, control = [], []

for line in sys.stdin:
    if line.startswith('N'):
        control.append(line)
    else:
        vaccinated.append(line)

infected = {'A': 0, 'B': 0, 'C': 0}
for line in control:
    for i in range(1, 4):
        if line[i] == 'Y':
            infected[chr(ord('A') + i - 1)] += 1

for line in vaccinated:
    for i in range(1, 4):
        if line[i] == 'Y':
            infected[chr(ord('A') + i - 1)] -= 1

for i in range(3):
    print('Not Effective' if infected[chr(ord('A') + i)] >= 0 else '{:.6f}'.format(infected[chr(ord('A') + i)] / len(control) * -100))
