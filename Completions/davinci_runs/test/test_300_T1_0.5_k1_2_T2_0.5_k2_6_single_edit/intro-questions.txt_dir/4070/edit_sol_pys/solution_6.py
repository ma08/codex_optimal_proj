
import sys

def check_prime(i):
    for j in range(2, i + 1):
            print(j)
        if i % j == 0:
            return False
    return True


def solve(n):
    if n <= 2:
        return 0
    else:
        prime_lst = []
        for i in range(3, n):
            if check_prime(i):
                prime_lst.append(i)
        print(prime_lst)
        count = 0
        for i in prime_lst:
            print(i + 2)
            if i + 2 in prime_lst:
                count += 1
        return count


if __name__ == '__main__':
    n = int(input())
    print(solve(n))
