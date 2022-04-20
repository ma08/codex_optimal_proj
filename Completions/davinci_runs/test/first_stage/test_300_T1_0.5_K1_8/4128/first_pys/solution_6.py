

import sys

def solve(n):
    # find the number of ways to represent n as the sum of n=a+b, where a and b are positive integers and a>b
    # the number of ways to represent n as the sum of n=a+b, where a and b are positive integers and a>=b is
    # the number of ways to represent n as the sum of n=a+b, where a and b are non-negative integers
    # which is the number of ways to represent n-1 as the sum of n-1=a+b, where a and b are non-negative integers
    # which is the number of ways to represent n-1 as the sum of n-1=a+b, where a and b are positive integers and a>=b
    # which is the number of ways to represent n-1 as the sum of n-1=a+b, where a and b are positive integers and a>b
    return solve(n-1) if n > 1 else 0

def main():
    T = int(sys.stdin.readline())
    for _ in range(T):
        n = int(sys.stdin.readline())
        print(solve(n))

if __name__ == '__main__':
    main()