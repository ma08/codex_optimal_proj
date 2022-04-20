

def main():
    n, m = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(n)]

    print(edges)

if __name__ == '__main__':
    main()
