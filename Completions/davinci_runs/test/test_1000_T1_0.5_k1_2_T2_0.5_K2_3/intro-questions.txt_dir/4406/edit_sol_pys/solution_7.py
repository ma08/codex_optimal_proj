

def main():
    n, m = [int(x) for x in input().split()]
    matrix = [input() for i in range(n)]
    for i in range(m):
        for j in range(n):
            print(matrix[n - j - 1][i], end='')
        print()

if __name__ == '__main__':
    main()
