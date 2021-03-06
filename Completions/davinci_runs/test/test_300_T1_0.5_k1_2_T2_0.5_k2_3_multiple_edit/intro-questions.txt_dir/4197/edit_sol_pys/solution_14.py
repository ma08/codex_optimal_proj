
def main():
    n = int(input())
    a = list(map(int, input().split())) # Список с координатами по х
    b = list(map(int, input().split())) # Список с координатами по y
    a = list(enumerate(a, 1)) # Список с номером координаты и координатой по х
    a = sorted(a, key=lambda x: x[1]) # Список с координатами по х отсортированный по возрастанию
    a = [i[0] for i in a] # Список с номерами координат отсортированный по возрастанию координат по х
    b = [b[i-1] for i in a] # Список с координатами по y отсортированный по возрастанию координат по х
    print(*b, sep='\n') # Вывод отсортированных координат по y


if __name__ == '__main__':
    main()
