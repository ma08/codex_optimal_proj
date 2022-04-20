
def main():
    n, m = map(int, input().split())
    edges = []
    for i in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
    print("YES")  # 一番最初にYESと出力
    for i in range(m):
        if edges[i][0] < edges[i][1]:
            print("0", end="")  # 0を出力して改行しない
        else:
            print("1", end="")  # 1を出力して改行しない


if __name__ == "__main__":
    main()
