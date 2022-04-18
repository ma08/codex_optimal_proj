

def factorial(n):
    return n * factorial(n-1) if n > 1 else 1

def last_digit(n):
    return factorial(n) % 10

def main():
    test_cases = int(input())
    for i in range(test_cases):
        n = int(input())
        print(last_digit(n))

if __name__ == "__main__":
    main()
