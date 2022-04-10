
import math

def count_ones(n):
    return sum([int(math.log(n, 2)) + 1 for n in range(1, n + 1)])

def main():
    n = int(input())
    print(count_ones(n))

if __name__ == '__main__':
    main()