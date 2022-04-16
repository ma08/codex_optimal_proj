

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

def main():
    T = int(input())
    for i in range(T):
        N = int(input())
        print(str(factorial(N))[-1]) # print the last digit of the factorial

if __name__ == "__main__":
    main()
