
def solve(n, x, y, number, cache):
    operations = 0
    for i in range(n - x):
        if number[i] != number[i+x]:
            operations += 1

    return operations

def main():
    n, x, y = map(int, input().split())
    number = input()
    cache = {}
    print(solve(n, x, y, number, cache))


if __name__ == "__main__":
    main()
