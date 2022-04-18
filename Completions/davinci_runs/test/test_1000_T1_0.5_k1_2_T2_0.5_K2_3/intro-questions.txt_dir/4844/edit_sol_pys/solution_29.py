

def main():
    N = int(input())
    matrix = []
    for i in range(N):
        matrix.append(list(map(int, input().split())))
    arr = [0] * (N+1)
    for i in range(N-1):
        for j in range(i+1, N-1):
            arr[i+1] |= matrix[i][j] | matrix[i][j+1]
            arr[j+1] |= matrix[i][j] | matrix[i][j+1]
            arr[j+2] |= matrix[i][j] | matrix[i][j+1]
    for i in range(1, N+1):
        print(arr[i], end=' ')

if __name__ == "__main__":
    main()
