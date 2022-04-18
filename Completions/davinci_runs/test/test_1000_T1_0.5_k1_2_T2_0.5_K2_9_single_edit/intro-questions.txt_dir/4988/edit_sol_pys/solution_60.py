

def factorial(n):
    return 1 if n == 1 else n * factorial(n-1)

def last_digit(n):
    return factorial(n) % 10

def main():
    for i in range(int(input().strip())):
        n = int(input().strip())
        print(last_digit(n))

if __name__ == '__main__':
    main()
