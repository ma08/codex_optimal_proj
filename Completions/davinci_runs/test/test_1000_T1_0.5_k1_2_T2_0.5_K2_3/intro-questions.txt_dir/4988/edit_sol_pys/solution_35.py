

def fact(n):
    return 1 if n == 1 else n * fact(n-1)

def last_digit(n):
    return fact(n) % 10 if n > 0 else 1

def main():
    num_cases = int(input().strip())
    for i in range(num_cases):
        n = int(input().strip())
        print(last_digit(n))

if __name__ == '__main__':
    main()
