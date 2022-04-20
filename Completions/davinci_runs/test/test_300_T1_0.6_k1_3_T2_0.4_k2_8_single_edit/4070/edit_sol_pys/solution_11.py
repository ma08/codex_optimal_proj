

def get_sum_of_digits(n):
    s = 0
    while n > 0:
        s += n % 10
        n = n // 10
    return s

def get_sum_of_digits_of_powers(n, p):
    return sum(get_sum_of_digits(i) for i in range(1, n + 1) if i % p == 0)

def main():
    n = int(input())
    print(get_sum_of_digits_of_powers(n, 2))

if __name__ == '__main__':
    main()
