
def main():
    n = int(input())
    m = [[0] * n for i in range(n)]
    for i in range(n):
        m[i] = [int(x) for x in input().split()]
    a = [0] * n
    for i in range(n):
        for j in range(n):
            if i != j:
                a[i] = a[i] ^ m[i][j]
    print(*a)

if __name__ == "__main__":
    main()
