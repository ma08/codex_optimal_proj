

def main():
    k = int(input("Введите число: "))  # Введите число
    a = 0
    b = 1
    for i in range(k):
        a, b = b, a + b
    print(a, b)

if __name__ == "__main__":
    main()
