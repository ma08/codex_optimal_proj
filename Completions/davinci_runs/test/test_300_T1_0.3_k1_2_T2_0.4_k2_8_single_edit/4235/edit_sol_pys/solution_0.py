
def main():
    n, m = map(int, input().split())
    edges = []
    for i in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
    print("YES", end="\n")
    for u, v in edges:
        if u < v:
            print("0", end="\n")
        elif u > v:
            print("1", end="\n")


if __name__ == "__main__":
    main()
