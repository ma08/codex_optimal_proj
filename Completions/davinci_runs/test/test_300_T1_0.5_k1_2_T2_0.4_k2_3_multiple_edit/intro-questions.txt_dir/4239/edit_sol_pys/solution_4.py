
def main():
    n = int(input())
    count = 0
    while n > 0:
        if n % 6 != 0 and n % 9 != 0:
            n -= 1
            count += 1;
        n = max(n // 6, n // 9)
        count += 1
    print(count)

if __name__ == '__main__':
    main()
