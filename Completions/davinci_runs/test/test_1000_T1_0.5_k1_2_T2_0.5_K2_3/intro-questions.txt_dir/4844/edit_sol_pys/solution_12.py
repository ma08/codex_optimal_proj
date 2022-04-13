

def main():
    N = int(input())
    matrix = []
    for i in range(N):
        matrix.append(list(map(int, input().split())))
    arr = [0] * N
    for i in range(N-1):
        for j in range(i+1, N-1):
            arr[i] |= matrix[i][j] | matrix[j][i]
            arr[j] |= matrix[i][j] | matrix[j][i]
            arr[j+1] |= matrix[i][j] | matrix[j][i]
    for i in range(N):
        print(arr[i], end=' ')

if __name__ == "__main__":
    main()
