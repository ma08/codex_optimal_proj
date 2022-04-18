
import sys

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def euler_number(n):
    return sum([1/factorial(x) for x in range(n+1)])

if __name__ == "__main__":
    n = int(sys.argv[1])
    print("{:.10f}".format(euler_number(n)))
