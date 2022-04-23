

def solve(n, m, graph):
    return 0

def main():
    n, m = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    print(solve(n, m, graph))

if __name__ == '__main__':
    main()
