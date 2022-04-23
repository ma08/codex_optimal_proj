

def get_sum_of_digits(num):
    sum = 0
    while num > 0:
        sum += num % 10
        num = num // 10
    return sum

def get_sum_of_digits_of_powers(num):
    power = 1
    sum = 0
    while power <= num:
        sum += get_sum_of_digits(power)
        power *= 2
    return sum

def main():
    n = int(input())
    print(get_sum_of_digits_of_powers(n))

if __name__ == '__main__':
    main()
