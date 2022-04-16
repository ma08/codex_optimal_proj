

def factorial(N):
    if N <= 1:
        return 1
    else:
        return N*factorial(N-1)

def main():
    test_cases = int(input())
    for i in range(test_cases):
        N = int(input())
        print(str(factorial(N))[-1])

if __name__ == "__main__":
    main()
