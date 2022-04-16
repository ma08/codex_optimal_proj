

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

def main():
    T = int(input())
    for i in range(T):
        N = int(input())
        print(str(factorial(N))[-1])

if __name__ == "__main__":
    main()
