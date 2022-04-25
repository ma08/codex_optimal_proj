
def main():
    n, m = map(int, input().split())
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().split())))
    print(solve(n, m, matrix))

def solve(n, m, matrix):
    # First, find the minimum value in each row
    min_vals = [min(row[i] for row in matrix) for i in range(m)]
    # Now, the max diff is the max difference between any two elements in min_vals
    max_diff = 0
    for i in range(m):
        max_diff = max(max_diff, abs(min_vals[i] - min_vals[i + 1]))
    return max_diff

if __name__ == "__main__":
    main()
