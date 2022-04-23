

def main():
    n = int(input())
    doublets_count = 0
    for i in range(n):
        d1, d2 = map(int, input().split())  # разделяем входные данные на два числа
        if d1 == d2:
            doublets_count += 1  # если числа равны, то увеличиваем счетчик на 1
        else:  # если числа не равны, то обнуляем счетчик
            doublets_count = 0  
        if doublets_count == 3:
            break  # если счетчик достиг 3, то выходим из цикла
    if doublets_count == 3:
        print("Yes")  # если счетчик все еще равен 3, то выводим Yes
    else:
        print("No")  # иначе No

if __name__ == '__main__':
    main()
