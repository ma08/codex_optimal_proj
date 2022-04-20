


# TODO: implement the solution
def solve(k, n, a, b):
    return -1


# TODO: implement the parser
def parse():
    q = int(input())
    for _ in range(q):
        k, n, a, b = map(int, input().split())
        yield k, n, a, b


def main():
    for args in parse():
        print(solve(*args))


if __name__ == "__main__":
    main()