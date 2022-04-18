

def main():
    n = int(input())
    doublets_count = 0
    for i in range(n):
        d1, d2 = map(int, input().split())  # объявляет переменные и присваивает им значения
        if d1 == d2:
            doublets_count += 1  # прибавляет к переменной значение 1
        else:
            doublets_count = 0  # присваивает переменной значение 0
        if doublets_count == 3:
            break  # прерывает цикл
    if doublets_count == 3:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()
