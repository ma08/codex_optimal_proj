

def main():
    n = int(input())
    print(n // 2 / n if n % 2 == 0 else (n + 1) // 2 / n)

if __name__ == '__main__':
    main()
