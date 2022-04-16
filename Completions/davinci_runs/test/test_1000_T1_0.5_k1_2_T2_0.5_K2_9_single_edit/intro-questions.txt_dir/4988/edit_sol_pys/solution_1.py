

def main():
    num_test_cases = int(input())
    for _ in range(num_test_cases):
        n = int(input())
        print(factorial(n))

def factorial(n):
    if n < 2:
        return 1
    else:
        return (n * factorial(n - 1)) % 10

if __name__ == "__main__":
    main()
