
def main():
    N = int(input())
    matrix = list(map(int, input().split()))
    for i in range(N):
        matrix[i] = int(matrix[i])
    arr = [0] * N
    for i in range(N):
        for j in range(i+1, N):
            arr[i] |= matrix[i][j]
            arr[j] |= matrix[i][j]
    for i in range(N):
        print(arr[i], end=' ')

if __name__ == "__main__":
    main()
