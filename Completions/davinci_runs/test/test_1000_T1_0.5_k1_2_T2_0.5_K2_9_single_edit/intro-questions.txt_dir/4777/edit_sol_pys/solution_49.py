

def main():
    k = int(input("Введите номер числа Фибоначчи: "))
    a = 0
    b = 1
    for i in range(k):
        a, b = b, a + b
    print(f"Число Фибоначчи под номером {k} равно {a}")

if __name__ == "__main__":
    main()
