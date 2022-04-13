import math



def get_max_dist(n, k, matrix):
    # Implement your solution here
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                matrix[i][j] = 0
            else:
                matrix[i][j] = math.inf
    for i in range(k):
        for j in range(n):
            for k in range(n):
                matrix[j][k] = min(matrix[j][k], matrix[j][i] + matrix[i][k])

    max_dist = 0
    for i in range(n):
        for j in range(n):
            max_dist = max(max_dist, matrix[i][j])
    return max_dist


if __name__ == "__main__":
    n, k = [int(x) for x in input().split()]
    matrix = []
    for i in range(n):
        matrix.append([int(x) for x in input().split()])
    print(get_max_dist(n, k, matrix))
