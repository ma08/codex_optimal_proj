def main():
    n = int(input())
    for i in range(n):
        print(get_digit(int(input())))


def get_digit(n):
    n = 1
    while n > k:
        n -= k
        k += 1
    return str(k)[n-1]

if __name__ == "__main__":
    main()
