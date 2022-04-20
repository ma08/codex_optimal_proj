

def main():
    n = int(input())
    A = [int(i) for i in input().split()]
    D = min(A)  # поиск минимального элемента массива
    for i in range(n):
        A[i] = A[i] - D  # вычитаем из каждого элемента массива минимальный элемент
    if sum(A) % n == 0:
        print(D)  # выводим минимальный элемент
    else:
        print(-1)  # выводим -1

if __name__ == "__main__":
    main()
