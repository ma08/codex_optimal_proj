

from collections import Counter

def main():
    n = int(input())
    divisors = Counter(map(int, input().split()))
    x = 1
    y = 1
    for d in sorted(divisors):
        if divisors[d] == 1:
            x *= d
        else:
            x *= d
            y *= d
    print(x, y)

if __name__ == '__main__':
    main()