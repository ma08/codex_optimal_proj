

def get_sum_of_digits(n):
    s = 0
    for d in str(n):
        s += int(d)
    return s

def get_sum_of_digits_of_powers(n):
    s = 0
    for p in range(1, n + 1):
        s += get_sum_of_digits(p)
        p *= 2
    return s

def main():
    n = int(input())
    print(get_sum_of_digits_of_powers(n))

if __name__ == '__main__':
    main()
