

def solve(matrix):
    # Complete this function
    R, S = len(matrix), len(matrix[0])
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    result = 0
    for i in range(R):
        for j in range(S):
            if matrix[i][j] == "o":
                for d in directions:
                    if 0 <= i + d[0] < R and 0 <= j + d[1] < S:
                        if matrix[i + d[0]][j + d[1]] == "o":
                            result += 1
    return result // 2

if __name__ == "__main__":
    R, S = map(int, input().strip().split(' '))
    matrix = []
    for _ in range(R):
        matrix.append(list(input().strip()))
    result = solve(matrix)
    print(result)
