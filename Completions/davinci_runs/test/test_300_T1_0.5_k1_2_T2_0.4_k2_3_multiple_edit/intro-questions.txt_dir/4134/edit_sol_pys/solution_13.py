

def solve(n, m, k, graph):
    return 1

def main():
    n, m, k = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    print(solve(n, m, k, graph))

if __name__ == '__main__':
    main()
