


def solve(n, a, b):
    if b < 2*a:
        return (n//2) * b + (n%2) * a
    else:
        return n*a


def main():
    q = int(input())
    for _ in range(q):
        n, a, b = map(int, input().split())
        print(solve(n, a, b))

if __name__ == '__main__':
    main()
