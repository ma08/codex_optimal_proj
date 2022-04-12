
numbers = input().split()  # вводим числа и преобразуем их в список

for i in range(len(numbers)):
    numbers[i] = int(numbers[i])  # преобразуем элементы списка в числа
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
