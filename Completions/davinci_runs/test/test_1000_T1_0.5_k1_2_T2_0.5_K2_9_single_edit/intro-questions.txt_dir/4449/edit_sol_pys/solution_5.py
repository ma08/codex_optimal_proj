

from collections import Counter

def main():
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    print(solve(n, a))

def solve(n, a):
    count = Counter(a)
    return len([x for x in count.values() if x % 2])

if __name__ == "__main__":
    main()
