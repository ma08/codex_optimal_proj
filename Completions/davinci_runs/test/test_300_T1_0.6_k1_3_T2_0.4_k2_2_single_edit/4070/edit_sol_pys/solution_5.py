

def get_sum_of_digits(n):
    s = 0
    while n > 0:
        s += n % 10
        n = n // 10
    return s

def get_sum_of_digits_of_powers(n):
    p = 1
    s = 0
    while p <= n:
        s += get_sum_of_digits(p)
        p *= 2
    return s

def main():
    n = int(input())
    print(get_sum_of_digits_of_powers(n)

if __name__ == '__main__':
    main()
