

def main():
    h, w = map(int, input().split())
    matrix = [list(input()) for _ in range(h)]
    for i in range(h):
        for j in range(w):
            print(matrix[i][j], end='')
        print()
        print(matrix[i])

if __name__ == '__main__':
    main()
