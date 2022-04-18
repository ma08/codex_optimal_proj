

def fib(n:int) -> int:
    if n <= 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def main() -> None:
    k = int(input())
    a = fib(k + 1) - 1
    b = fib(k) - 1
    print(a, b)

if __name__ == "__main__":
    main()
