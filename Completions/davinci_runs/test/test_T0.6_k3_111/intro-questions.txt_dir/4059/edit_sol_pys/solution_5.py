
import math

def main():
    N = int(input())
    
    # The number of tuples that satisfy A * B - C = N.
    ans = 0
    
    # We enumerate all possible values of A and B.
    # Note that A * B - C = N.
    # Thus, in order to maximize the value of A * B,
    # it is enough to consider A = B,
    # because A * B - C = A * A - C = (A-C)(A+C).
    for a in range(1, math.ceil(math.sqrt(N))+1):
        # If a*a+1 == N, then a+1 is a factor of N.
        # Thus, a+1 is a factor of (a*a+1-N),
        # and the number of factors of N that are not a+1 is
        # the number of factors of (a*a+1-N) that are not a+1.
        if a*a + 1 == N:
            ans += len(factors(N))-1
        # If a*a == N, then a is a factor of N.
        # Thus, a is a factor of (a*a-N),
        # and the number of factors of N that are not a is
        # the number of factors of (a*a-N) that are not a.
        elif a*a == N:
            ans += len(factors(N))-1
        # Otherwise, a*a < N < (a+1)*(a+1).
        # Thus, a*a < N < a*a+2*a+1.
        # We can show that N-a*a is a factor of N.
        # This is because a*a < N < a*a+2*a+1,
        # so N-a*a = 2*a+1.
        # It is also easy to show that a is a factor of N.
        # Thus, the number of factors of N that are not a or N-a*a is
        # the number of factors of (a*a-N) that are not a.
        else:
            ans += len(factors(a*a-N))-1
    
    print(ans)

# Returns the list of all factors of n.
def factors(n):
    factors = []
    for i in range(1, math.ceil(math.sqrt(n))+1):
        if n % i == 0:
            factors.append(i)
            factors.append(n//i)
    return sorted(factors)

if __name__ == '__main__':
    main()
