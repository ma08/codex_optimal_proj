

def main():
    n = int(input())
    count = 1
    while n > 0:
        if n % 6 == 0:
            n = n // 6
        elif n % 9 == 0:
            n = n // 9
        else:
            n = n - 1
    print(count)

if __name__ == '__main__':
    main()
