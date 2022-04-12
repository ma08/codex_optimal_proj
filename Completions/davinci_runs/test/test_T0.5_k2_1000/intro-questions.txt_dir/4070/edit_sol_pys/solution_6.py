# check if a number is prime
import sys


def check_prime(i):
    for j in range(2, i//2):
        if i % j == 0:
            return False
    return True


# solve the problem

# if n is less than 2, there is no prime pair

# if n is 3, there is only one prime pair
def solve(n):
    if n <= 2:
# if n is greater than 3, we need to find the prime pairs
        return 0
    elif n == 3:
        return 1
    else:
        prime_lst = []
        for i in range(2, n+1):
            if check_prime(i):
                prime_lst.append(i)
        count = 0
        for i in prime_lst:
            if i + 2 in prime_lst:
                count += 1
        return count


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    print(solve(n))
