

N = int(input())
vaccinated = [0,0,0,0]
control = [0,0,0,0]

for i in range(N):
    line = input().strip()
    if line[0] == '1':
        vaccinated[0] += 1
        if line[1] == '1':
            vaccinated[1] += 1
        if line[2] == '1':
            vaccinated[2] += 1
        if line[3] == '1':
            vaccinated[3] += 1
    else:
        control[0] += 1
        if line[1] == '1':
            control[1] += 1
        if line[2] == '1':
            control[2] += 1
        if line[3] == '1':
            control[3] += 1

print(format((vaccinated[1]/vaccinated[0])/(control[1]/control[0])*100, '.6f'))
print(format((vaccinated[2]/vaccinated[0])/(control[2]/control[0])*100, '.6f'))
print(format((vaccinated[3]/vaccinated[0])/(control[3]/control[0])*100, '.6f'))
