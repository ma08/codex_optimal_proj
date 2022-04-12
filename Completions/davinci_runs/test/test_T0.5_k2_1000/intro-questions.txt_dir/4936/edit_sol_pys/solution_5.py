

def main():
    n = int(input())
    temps = list(map(int, input().split()))  # преобразование в список

    max_temp = 0  # максимальная температура
    day = 0

    for i in range(n - 2):
        temp = max(temps[i], temps[i + 1], temps[i + 2])  # нахождение максимальной температуры

        if temp > max_temp:
            max_temp = temp
            day = i + 1

    print(day, max_temp)

if __name__ == "__main__":
    main()
