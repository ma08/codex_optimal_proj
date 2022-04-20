


def main():
    n, m = map(int, input().split())
    edges = []
    for i in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
    print("YES")
    for i in range(m):
        if edges[i][0] < edges[i][1]:
            print("0", end="")
        else:
            print("1", end="")


if __name__ == "__main__":
    main()