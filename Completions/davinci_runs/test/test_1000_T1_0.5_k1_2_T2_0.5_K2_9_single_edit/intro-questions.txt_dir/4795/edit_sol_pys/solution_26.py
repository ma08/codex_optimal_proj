

with open('input.txt', 'r') as file:
    N = int(file.readline())
    output = 0
    for i in range(N):
        pow = 0
        number = file.readline()
        for i in range(len(number)):
            pow += int(number[i])
        output += pow ** len(number)
    print(output)
