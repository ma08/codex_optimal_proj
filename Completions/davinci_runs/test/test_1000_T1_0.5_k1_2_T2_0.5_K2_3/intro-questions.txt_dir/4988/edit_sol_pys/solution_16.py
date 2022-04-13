


def factorial(n):  # function to calculate factorial
    if n <= 1:
        return 1
    else:
        return n*factorial(n-1)  # recursion


def main():
    T = int(input())  # number of test cases
    for i in range(T):
        N = int(input())  # input number
        print(str(factorial(N))[-1])  # print last digit of factorial

if __name__ == "__main__":
    main()
