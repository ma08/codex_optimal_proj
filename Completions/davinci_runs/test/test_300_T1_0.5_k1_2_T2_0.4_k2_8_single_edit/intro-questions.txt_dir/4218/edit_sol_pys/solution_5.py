

def main():
    n = int(input())
    if n % 2 == 0:
        print(n // 2 / n)
    else:
        print((n + 1) // 2 / n)

if __name__ == '__main__':
    main()
