

def main():
    '''
    Read the number of test cases, then read each test case, and print the last
    digit of the factorial of the test case.
    '''
    num_test_cases = int(input('enter the number of test cases: '))
    for i in range(num_test_cases):
        n = int(input('enter '+str(i)+'th test case: '))
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
