

def solver(n, m, a):
    return 0


if __name__ == "__main__":
    n = int(input())
    m = int(input())
    a = [list(map(int, input().split())) for _ in range(m)]
    print(solver(n, m, a))
