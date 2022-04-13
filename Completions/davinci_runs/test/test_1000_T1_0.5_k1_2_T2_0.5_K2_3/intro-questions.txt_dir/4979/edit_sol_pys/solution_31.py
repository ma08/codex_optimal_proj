

def reverse_binary(n):  # функция для переворачивания бинарного кода
    return int(bin(n)[2:][::-1], 2)  # переворачиваем бинарный код, приводим к числу и возвращаем

if __name__ == "__main__":
    print(reverse_binary(int(input())))  # выводим результат
