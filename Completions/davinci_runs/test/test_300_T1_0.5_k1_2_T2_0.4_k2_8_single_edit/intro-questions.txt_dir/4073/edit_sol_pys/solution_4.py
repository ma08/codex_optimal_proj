

def main():
    # Get input
    n, m = [int(x) for x in input().split()]

    # Solve
    print(solve(n, m))

def solve(n, m):
    # Find the number of groups
    groups = 1
    while n > m:
        n -= m
        groups += 1

    # Return the number of groups
    return groups

if __name__ == '__main__':
    main()
