

def main():
    N = int(input())
    matrix = []
    for i in range(N):
        matrix.append(list(map(int, input().split())))
    arr = [0] * N
    for i in range(N-1):
        for j in range(i+1, N-1):
            arr[i] |= matrix[i][j]
            arr[j] |= matrix[i][j]
            arr[j+1] |= matrix[i][j+1]
    for i in range(N):
        print(arr[i], end=' ')

if __name__ == "__main__":
    main()
