
import sys

def check_prime(i):
    for j in range(2, i):
        if i % j == 0:
            return False
    return True


def solve(n):
    if n <= 2: return 0
    elif n == 3: return 1
    prime_list = []
    for i in range(2, n):
        if check_prime(i):
            prime_list.append(i)
    count = 0
    for i in prime_list:
        if i + 2 in prime_list:
            count += 1
    return count


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    print(solve(n))
