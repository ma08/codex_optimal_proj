

N = int(input())

output = 0
for i in range(N):
    power = 0
    number = input()
    for i in range(len(number)):
        power += int(number[i])
    output += power ** len(number)
print(output)
