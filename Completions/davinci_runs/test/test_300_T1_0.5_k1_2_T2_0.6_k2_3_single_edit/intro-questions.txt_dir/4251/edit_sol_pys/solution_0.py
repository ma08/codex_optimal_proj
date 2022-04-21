
def main():
    n, m = map(int, input().split())
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().split())))
    print(solve(n, m, matrix), end='')

def solve(n, m, matrix):
    # TODO
    pass

if __name__ == "__main__":
    main()
