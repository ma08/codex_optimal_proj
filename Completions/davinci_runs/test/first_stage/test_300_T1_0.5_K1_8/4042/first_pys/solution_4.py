

def main():
    n = float(input())
    n = n % 1
    n = n * 100

    a = int(n / 10)
    b = int(n % 10)

    print(a, b)

if __name__ == '__main__':
    main()