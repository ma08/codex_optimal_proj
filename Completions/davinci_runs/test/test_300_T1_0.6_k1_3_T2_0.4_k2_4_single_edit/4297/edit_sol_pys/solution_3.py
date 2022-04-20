
def solve(N):
    if N % 2 == 0:
        return N
    else:
        return 2 * N


def main():
    N = int(input())
    print(solve(N))


if __name__ == "__main__":
    main()
