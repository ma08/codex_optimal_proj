import sys


def main():
    n, m = map(int, input().split())
    edges = []
    for i in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
    sys.stdout.write("YES\n")
    for i in range(m):
        if edges[i][0] < edges[i][1]:
            sys.stdout.write("0")
        else:
            sys.stdout.write("1")
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
