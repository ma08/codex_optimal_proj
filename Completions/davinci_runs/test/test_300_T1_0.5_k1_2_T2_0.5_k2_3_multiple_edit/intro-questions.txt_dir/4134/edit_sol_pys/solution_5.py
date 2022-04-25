

def solve(n, m, k, mat):
    return 1

def main():
    n, m, k = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(n)]
    print(solve(n, m, k, mat))

if __name__ == '__main__':
    main()
