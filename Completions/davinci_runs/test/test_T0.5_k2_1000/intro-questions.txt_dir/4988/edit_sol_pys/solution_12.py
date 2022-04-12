

def factorial(n, m=10):
    return n * factorial(n-1, m) % m

def last_digit(n):
    return factorial(n) % 10

def main():
    num_cases = int(input().strip())
    for i in range(num_cases):
        n = int(input().strip())
        print(last_digit(n))

if __name__ == '__main__':
    main()
