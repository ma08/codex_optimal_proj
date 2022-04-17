


import sys

def check_prime(i):
    for j in range(2, i):
        if i % j == 0:
            return False
    return True


def solve(n):
    prime_lst = []
    for i in range(2, n):
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
