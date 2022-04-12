

def fib(n): # function for calculating fibonacci numbers
    if n <= 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def main():
    k = int(input()) # input
    a = fib(k + 1) - 1 # calculating the number of rabbits at the end of the month
    b = fib(k) - 1 # calculating the number of rabbits at the beginning of the month
    print(a, b)

main()
