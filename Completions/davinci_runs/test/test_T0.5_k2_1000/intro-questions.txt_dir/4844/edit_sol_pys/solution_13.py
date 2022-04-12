

def main():
    n = int(input())
    matrix = []
    for i in range(n):
        matrix.append([int(x) for x in input().split()])
    a = [0] * (n + 1)
    for i in range(n):
        for j in range(n):
            a[i] = a[i] ^ matrix[i][j]
    print(*a)

if __name__ == "__main__":
    main()
