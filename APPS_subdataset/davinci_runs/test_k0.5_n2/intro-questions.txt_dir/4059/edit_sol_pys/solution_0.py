

# This is a simple problem, but it is important to note that the number of divisors is equal to the number of divisors of N.

N = int(input())

def count_divisors(N):
    count = 0
    for i in range(1, N+1):
        if N % i == 0:
            count += 1
    return count

print(count_divisors(N))
