
N = int(input())
output = 0
for i in range(N):
    pow = 0
    number = input()
    for i in range(len(number)):
        pow += int(number[i])
    output += pow ** len(number)
print(output)
