

def main():
    n = int(input())
    a = list(map(int, input().split()))  # список из введенных чисел, преобразованных в int
    for i in range(n-1):  # проверяем на соседство одинаковых чисел
        if a[i] == a[i+1]:  # если соседние числа одинаковые
            a[i] += 1  # то увеличиваем их на 1
            a[i+1] += 1  # и увеличиваем их на 1
    if len(set(a)) == 1:  # если все числа одинаковые
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()
