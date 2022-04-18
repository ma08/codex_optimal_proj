

def main():
    '''
    Reads the number of test cases, then reads each test case, and prints the
    last digit of the factorial of the test case.
    '''
    num_test_cases = int(input())
    for _ in range(num_test_cases):
        n = int(input())
        print(factorial(n))


if __name__ == "__main__":
    main()
