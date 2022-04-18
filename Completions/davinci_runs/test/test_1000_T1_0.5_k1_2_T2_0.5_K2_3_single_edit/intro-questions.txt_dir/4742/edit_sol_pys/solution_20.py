import math


def main():
    n = int(input())
    for i in range(n):
        x = int(input())
        s = 0
        for j in range(1, x + 1):
            s += math.factorial(x) / math.factorial(j)
        print(int(s))


if __name__ == '__main__':
    main()
