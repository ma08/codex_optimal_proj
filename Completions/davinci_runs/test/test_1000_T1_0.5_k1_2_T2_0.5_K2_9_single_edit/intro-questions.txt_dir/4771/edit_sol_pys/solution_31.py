

def main():
    # Get input and convert to integers
    n = int(input())
    m = int(input())
    # Create matrix
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().split())))
    # Check if matrix is symmetric
    symmetric = True
    for i in range(n):
        for j in range(m):
            if matrix[i][j] != matrix[j][i]:
                symmetric = False
    # Print result
    if symmetric:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()
