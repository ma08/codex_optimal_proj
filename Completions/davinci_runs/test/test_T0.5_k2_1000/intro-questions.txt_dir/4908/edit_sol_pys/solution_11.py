numbers = input().split()

for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

if numbers[0] + numbers[1] == numbers[2]:
    print(str(numbers[0]) + "+" + str(numbers[1]) + "=" + str(numbers[2]))
elif numbers[0] - numbers[1] == numbers[2]:
    print(str(numbers[0]) + "-" + str(numbers[1]) + "=" + str(numbers[2]))
elif numbers[0] * numbers[1] == numbers[2]:
    print(str(numbers[0]) + "*" + str(numbers[1]) + "=" + str(numbers[2]))
elif numbers[0] / numbers[1] == numbers[2]:
    print(str(numbers[0]) + "/" + str(numbers[1]) + "=" + str(numbers[2]))
elif numbers[2] + numbers[1] == numbers[0]:
    print(str(numbers[0]) + "=" + str(numbers[1]) + "+" + str(numbers[2]))
elif numbers[2] - numbers[1] == numbers[0]:
    print(str(numbers[0]) + "=" + str(numbers[1]) + "-" + str(numbers[2]))
elif numbers[2] * numbers[1] == numbers[0]:
    print(str(numbers[0]) + "=" + str(numbers[1]) + "*" + str(numbers[2]))
elif numbers[2] / numbers[1] == numbers[0]:
    print(str(numbers[0]) + "=" + str(numbers[1]) + "/" + str(numbers[2]))
