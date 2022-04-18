

def main():
    N = int(input())
    matrix = []
    for i in range(N):
        matrix.append(list(map(int, input().split())))
    arr = [0] * (N+1)
    for i in range(N):
        for j in range(i+1, N):
            arr[i] |= matrix[i][j]
            arr[j] |= matrix[i][j]
    for i in range(N):
        print(arr[i], end=' ')

if __name__ == "__main__":
    main()
