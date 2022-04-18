

numbers = input().split()
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])


def check(numbers, i, j, k):
    if numbers[i] + numbers[j] == numbers[k]:
        print(str(numbers[i]) + "+" + str(numbers[j]) + "=" + str(numbers[k]))
    elif numbers[i] - numbers[j] == numbers[k]:
        print(str(numbers[i]) + "-" + str(numbers[j]) + "=" + str(numbers[k]))
    elif numbers[i] * numbers[j] == numbers[k]:
        print(str(numbers[i]) + "*" + str(numbers[j]) + "=" + str(numbers[k]))
    elif numbers[i] / numbers[j] == numbers[k]:
        print(str(numbers[i]) + "/" + str(numbers[j]) + "=" + str(numbers[k]))


check(numbers, 0, 1, 2)
check(numbers, 2, 1, 0)
