
def main():
    n, m = map(int, input().split())
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().split())))
    print(solve(n, m, matrix))

def solve(n, m, matrix):
    # First, find the maximum value in each column
    max_vals = [max(row[i] for row in matrix) for i in range(m)]
    # Now, the min k is the min difference between any two elements in max_vals
    min_k = 0
    for i in range(m - 1): 
        min_k = min(min_k, abs(max_vals[i] - max_vals[i + 1]))
    return min_k

if __name__ == "__main__":
    main()
