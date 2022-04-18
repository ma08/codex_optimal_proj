

N = int(input())
output = 0
for i in range(N):
    pow = 0
    number = input()
    for j in range(len(number)):
        pow += int(number[j])
    output += pow ** len(number)
print(output)
