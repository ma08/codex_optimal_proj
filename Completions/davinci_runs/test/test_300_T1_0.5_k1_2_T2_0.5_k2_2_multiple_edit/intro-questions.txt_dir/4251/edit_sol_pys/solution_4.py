import math

def main():
    n, m = map(int, input().split()) # n = num rows, m = num cols
    matrix = [] # matrix[i] = ith row of matrix
    for _ in range(n): # read in the matrix
        matrix.append(list(map(int, input().split()))) # matrix[i][j] = element in ith row, jth col
    print(solve(n, m, matrix)) # solve the problem

def solve(n, m, matrix):
    # First, find the minimum value in each col
    min_vals = [min(row[i] for row in matrix) for i in range(m)] # min_vals[i] = min val in ith col
    # Now, the max k is the max difference between any two elements in min_vals (i.e. any two cols)
    max_k = 0
    for i in range(m - 1): # iterate through all pairs of cols
        max_k = max(max_k, abs(min_vals[i] - min_vals[i + 1])) # update max_k
    return max_k

if __name__ == "__main__":
    main()
