

def sum_of_digits(n):
    return sum(int(x) for x in str(n))

def main():
    n = int(input())
    while n % sum_of_digits(n) != 0:
        n += 1
    print(n)

if __name__ == '__main__':
    main()
