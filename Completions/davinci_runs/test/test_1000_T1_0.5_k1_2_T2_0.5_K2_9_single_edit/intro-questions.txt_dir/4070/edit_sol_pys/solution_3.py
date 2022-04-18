
import sys
import math

def check_prime(i):
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0:
            return False
    return True


def solve(n):
    if n <= 2:
        return 0
    else:
        prime_lst = []
        for i in range(3, n, 2):
            if check_prime(i):
                prime_lst.append(i)
        prime_lst.append(2)
        count = 0
        for i in prime_lst:
            if i + 2 in prime_lst:
                count += 1
        return count


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    print(solve(n))
