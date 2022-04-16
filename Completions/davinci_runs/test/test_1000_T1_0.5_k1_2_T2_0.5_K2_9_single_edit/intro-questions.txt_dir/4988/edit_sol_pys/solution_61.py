

def main(file_name):
    '''
    Reads the number of test cases, then reads each test case, and prints the
    last digit of the factorial of the test case.
    '''
    file = open(file_name, 'r')
    num_test_cases = int(file.readline())
    for _ in range(num_test_cases):
        n = int(file.readline())
    file.close()
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
    main(sys.argv[1])
