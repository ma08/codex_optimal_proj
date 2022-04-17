import math


def s(n):  # sieve of eratosthenes
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * 2, n+1, p):
                prime[i] = False
        p += 1
    prime[0]= False
    prime[1]= False
    return prime

def sieve(n):
    prime = s(n)
    for p in range(n+1):
        if prime[p]:
            print(p, end=" ")
    print()

def main():
    n = int(input())  # number of test cases
    for i in range(n):
        m = int(input())
        sieve(m)

main()
