

N = int(input())
output = 0
for i in range(N):
    power = 0
    number = input()
    for j in range(len(number)):
        power += int(number[j])
    output += power ** len(number)
print(output)
