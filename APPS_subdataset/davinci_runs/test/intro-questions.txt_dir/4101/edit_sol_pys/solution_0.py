
def main():
    n, m = [int(x) for x in input().split()]  # read n and m
    matrix = []
    for i in range(n):  # read matrix
        matrix.append([int(x) for x in input().split()])

    rows = [0] * n  # rows and columns
    columns = [0] * m  # rows and columns
    for i in range(n):  # count rows and columns
        for j in range(m):
            if matrix[i][j] == 1:
                rows[i] += 1
                columns[j] += 1

    for i in range(n):
        for j in range(m):
            if (rows[i] + columns[j]) % 2 != matrix[i][j]:
                print("NO")
                return
    print("YES")
    print(" ".join(["1" if x % 2 == 1 else "0" for x in rows]))
    print(" ".join(["1" if x % 2 == 1 else "0" for x in columns]))

if __name__ == "__main__":
    main()
