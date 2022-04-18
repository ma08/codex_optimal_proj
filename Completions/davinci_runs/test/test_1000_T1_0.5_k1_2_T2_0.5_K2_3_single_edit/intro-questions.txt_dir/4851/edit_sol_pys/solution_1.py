

def sum_digits(n):
    return sum(int(x) for x in n)

def main():
    n = int(input())
    while n % sum_digits(str(n)) != 0:
        n += 1
    print(n)

if __name__ == '__main__':
    main()
