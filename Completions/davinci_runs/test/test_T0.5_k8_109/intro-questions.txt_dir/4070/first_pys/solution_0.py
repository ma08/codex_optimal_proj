

import math

def solve(n):
    divisors = []
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            divisors.append(i)
            divisors.append(n//i)
    return len(set(divisors))

def main():
    n = int(input())
    print(solve(n))

main()