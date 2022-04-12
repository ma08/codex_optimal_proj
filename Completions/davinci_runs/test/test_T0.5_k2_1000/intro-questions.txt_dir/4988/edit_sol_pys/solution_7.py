

def main():
    '''
    Reads the number of test cases, then reads each test case, and prints the
    last digit of the factorial of the test case.
    '''
    num_test_cases = int(input('Enter number of test cases: '))
    for _ in range(num_test_cases):
        n = int(input('Enter a number: '))
        print(factorial(n))

def factorial(n):
    '''
    Computes the last digit of n!
    '''
    if n < 2:
        return 1
    else:
        return (n * factorial(n - 1)) % 10

if __name__ == "__main__":
    main()
