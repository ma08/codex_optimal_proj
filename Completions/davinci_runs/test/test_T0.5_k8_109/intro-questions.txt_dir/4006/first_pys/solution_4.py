


def main():
    n = int(input())
    result = 10
    if n < 10:
        result = n
    if n > 10:
        result += 9
        if n % 10 == 0:
            result += 1
    print(result)

if __name__ == '__main__':
    main()