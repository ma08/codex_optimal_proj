

def main():
    N = int(input())
    matrix = []
    for i in range(0, N):
        matrix.append([int(x) for x in input().split()])
    array = [None] * N
    for i in range(0, N):
        for j in range(0, N):
            if i != j and matrix[i][j] != 0:
                if array[i] is None:
                    array[i] = matrix[i][j]
                if array[j] is None:
                    array[j] = matrix[i][j]
                if array[i] != matrix[i][j] or array[j] != matrix[i][j]:
                    array[i] = -1
                    array[j] = -1
                    break
    for i in range(0, N):
        if array[i] is None:
            array[i] = 0
    print(" ".join(str(x) for x in array))

if __name__ == "__main__":
    main()