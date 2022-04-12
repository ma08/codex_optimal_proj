

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n*factorial(n-1)

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        print(str(factorial(n))[-1])

if __name__ == "__main__":
    main()
