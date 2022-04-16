#!/usr/bin/python3

# Problem

# A prime is a positive integer X that has exactly two distinct divisors: 1 and X.
# The first few prime integers are 2, 3, 5, 7, 11 and 13.

# A semiprime is a natural number that is the product of two (not necessarily distinct) prime numbers.
# The first few semiprimes are 4, 6, 9, 10, 14, 15, 21, 22, 25, 26.

# You are given two non-empty arrays P and Q, each consisting of M integers.
# These arrays represent queries about the number of semiprimes within specified ranges.

# Query K requires you to find the number of semiprimes within the range (P[K], Q[K]), where 1 ≤ P[K] ≤ Q[K] ≤ N.

# For example, consider an integer N = 26 and arrays P, Q such that:

#     P[0] = 1    Q[0] = 26
#     P[1] = 4    Q[1] = 10
#     P[2] = 16   Q[2] = 20
# The number of semiprimes within each of these ranges is as follows:

# (1, 26) is 10,
# (4, 10) is 4,
# (16, 20) is 0.
# Write a function:

# def solution(N, P, Q)

# that, given an integer N and two non-empty arrays P and Q consisting of M integers,
# returns an array consisting of M elements specifying the consecutive answers to all the queries.

# For example, given an integer N = 26 and arrays P, Q such that:

#     P[0] = 1    Q[0] = 26
#     P[1] = 4    Q[1] = 10
#     P[2] = 16   Q[2] = 20
# the function should return the values [10, 4, 0], as explained above.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [1..50,000];
# M is an integer within the range [1..30,000];
# each element of arrays P, Q is an integer within the range [1..N];
# P[i] ≤ Q[i].



# Solution

def solution(N, P, Q):

    # write your code in Python 3.6
    # a semiprime is a product of two primes, so we can find the semiprimes
    # by finding the primes, then finding the products of the primes

    # first find the primes
    primes = [True] * (N+1)
    primes[0] = False
    primes[1] = False

    for i in range(2,N+1):
        if primes[i]:
            for j in range(i*i,N+1,i):
                primes[j] = False

    # now find the semiprimes
    semiprimes = [False] * (N+1)
    for i in range(1,N+1):
        for j in range(i,N+1):
            if primes[i] and primes[j] and i*j <= N:
                semiprimes[i*j] = True

    # now for each query, count the number of semiprimes in the range
    M = len(P)
    answers = [0] * M
    for i in range(M):
        for j in range(P[i],Q[i]+1):
            if semiprimes[j]:
                answers[i] += 1

    return answers





































































































































































































































































































































































































































































































