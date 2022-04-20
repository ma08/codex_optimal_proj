

import sys

def main():
    n = int(sys.stdin.readline())
    for i in range(n):
        line = sys.stdin.readline()
        line = line.split()
        n = int(line[0])
        k = int(line[1])
        min_packs = n
        for i in range(1, k+1):
            if n % i == 0:
                packs = n / i
                if packs < min_packs:
                    min_packs = packs
        print(min_packs)


if __name__ == "__main__":
    main()