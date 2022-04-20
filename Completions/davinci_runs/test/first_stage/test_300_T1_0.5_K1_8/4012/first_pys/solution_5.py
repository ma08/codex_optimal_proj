

import sys

def main():
    f = open(sys.argv[1])
    t = int(f.readline())
    for _ in range(t):
        a, b, c = map(int, f.readline().split())
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