

def min_expense(N, A, B):

    if N * A <= B:
        return N * A
    else:
        return B


def main():
    import sys
    N, A, B = map(int, sys.stdin.readline().rstrip().split())
    print(min_expense(N, A, B))


if __name__ == "__main__":
    main()
