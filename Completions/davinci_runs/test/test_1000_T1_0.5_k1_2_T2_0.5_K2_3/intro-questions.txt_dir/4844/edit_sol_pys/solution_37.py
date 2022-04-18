

def main():
    n = int(input())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().split())))
    arr = [0] * n
    for i in range(n):
        for j in range(i+1, n):
            arr[i] |= matrix[i][j]
            arr[j] |= matrix[i][j]
    for i in range(n):
        print(arr[i], end=' ')

if __name__ == "__main__":
    main()
