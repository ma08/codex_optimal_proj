

def factorial(m):
    if m < 2:
        return m
    return m * factorial(m-1)

def last_digit(n):
    return factorial(n) % 10

def main():
    test_cases = int(input())
    for i in range(test_cases):
        n = int(input())
        print(last_digit(n))

if __name__ == "__main__":
    main()
