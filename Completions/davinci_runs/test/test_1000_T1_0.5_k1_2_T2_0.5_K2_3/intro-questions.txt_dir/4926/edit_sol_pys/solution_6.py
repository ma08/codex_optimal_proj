
from math import factorial

def euler(n):
    return sum(1/factorial(i) for i in range(n+1))

if __name__ == '__main__':

    print(euler(int(input())))
