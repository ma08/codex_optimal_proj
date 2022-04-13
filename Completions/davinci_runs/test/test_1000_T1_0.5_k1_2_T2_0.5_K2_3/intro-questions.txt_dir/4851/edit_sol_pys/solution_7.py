

def sum_digits(num):
    return sum([int(x) for x in str(num)])

def main():
    n = input()
    while n % sum_digits(n) != 0:
        n += 1
    print(n)

if __name__ == '__main__':
    main()
