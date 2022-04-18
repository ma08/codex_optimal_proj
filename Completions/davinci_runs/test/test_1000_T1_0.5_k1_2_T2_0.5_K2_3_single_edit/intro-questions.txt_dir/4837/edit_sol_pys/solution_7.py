

import sys, math

def main():
    print(prime_factors(600851475143))

def compare(sven, friend):
    score = 0
    for i in range(len(sven)):
        if sven[i] == friend[i]:
            score += 1
        elif sven[i] == "R" and friend[i] == "S":
            score += 2
        elif sven[i] == "S" and friend[i] == "P":
            score += 2
        elif sven[i] == "P" and friend[i] == "R":
            score += 2
    return score

def max_compare(sven, friend):
    score = 0
    for i in range(len(sven)):
        if sven[i] == friend[i]:
            score += 1
        elif sven[i] == "R" and friend[i] == "S":
            score += 2
        elif sven[i] == "S" and friend[i] == "P":
            score += 2
        elif sven[i] == "P" and friend[i] == "R":
            score += 2
        elif sven[i] == "R" and friend[i] == "P":
            score += 0
        elif sven[i] == "S" and friend[i] == "R":
            score += 0
        elif sven[i] == "P" and friend[i] == "S":
            score += 0
    return score

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

if __name__ == '__main__':
    main()
