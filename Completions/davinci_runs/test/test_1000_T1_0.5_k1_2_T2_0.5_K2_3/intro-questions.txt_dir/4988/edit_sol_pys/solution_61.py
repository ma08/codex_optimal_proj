

def factorial(n):
    if n == 1:
        return 1 
    return n * factorial(n-1)

def last_digit(k):
    return factorial(k) % 10

def main():
    test_cases = int(input())
    for i in range(test_cases):
        k = int(input())
        print(last_digit(k))

if __name__ == "__main__":
    main()
