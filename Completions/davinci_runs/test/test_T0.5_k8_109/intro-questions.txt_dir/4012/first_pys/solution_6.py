

import sys

def main():
    num_tests = int(sys.stdin.readline())
    for _ in range(num_tests):
        a, b, c = [int(x) for x in sys.stdin.readline().split()]
        res = 0
        while b % a != 0:
            b += 1
            res += 1
        while c % b != 0:
            c += 1
            res += 1
        print(res)
        print(a, b, c)

if __name__ == "__main__":
    main()