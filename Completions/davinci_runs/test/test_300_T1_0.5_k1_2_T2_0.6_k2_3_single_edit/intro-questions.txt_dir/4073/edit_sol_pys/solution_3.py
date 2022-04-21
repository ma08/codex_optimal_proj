

def main():
    # Get input
    n = int(input())
    a = [int(x) for x in input().split()]

    # Solve
    print(solve(n, a, k))

def solve(n, a, k):
    # Sort a
    a = sorted(a)


if __name__ == '__main__':
    main()
