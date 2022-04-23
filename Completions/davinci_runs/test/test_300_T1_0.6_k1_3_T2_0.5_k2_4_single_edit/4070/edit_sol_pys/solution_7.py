
def get_sum_of_digits(n):
    s = 0
    while n:
        s += n % 10
        n = n // 10
    return s

def get_sum_of_digits_of_powers(n):
    p = 1
    s = 0
    while p <= n and p < 10**9:
        s += get_sum_of_digits(p)
        p *= 2
    return s

def main():
    n = int(input("Enter a number: "))
    print(get_sum_of_digits_of_powers(n))

if __name__ == '__main__':
    main()
