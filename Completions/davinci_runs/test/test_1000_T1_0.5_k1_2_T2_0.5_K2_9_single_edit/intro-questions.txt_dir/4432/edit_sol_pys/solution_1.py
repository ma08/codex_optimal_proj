import sys
import math



def get_next_prime(n):
    if n <= 1:
        return 2
    for i in range(n+1, 2*n):
        for j in range(2, int(math.sqrt(i))+1):
            if i % j == 0:
                break
        else:
            return i
    return -1

def main(n):
    if n == 1:
        return 1
    return get_next_prime(n)


def main2():
    for line in sys.stdin:
        n = int(line.strip())
        print(main(n))


if __name__ == "__main__":
    main2()
