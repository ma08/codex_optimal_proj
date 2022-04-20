


def main():
    n, m = map(int, input().split())  # type: int, int
    edges = []
    for i in range(m):
        u, v = map(int, input().split())  # type: int, int
        edges.append((u, v))
    print("YES")
    for i in range(m):
        if edges[i][0] < edges[i][1]:
            print("0", end="")  # type: str
        else:
            print("1", end="")  # type: str


if __name__ == "__main__":
    main()
