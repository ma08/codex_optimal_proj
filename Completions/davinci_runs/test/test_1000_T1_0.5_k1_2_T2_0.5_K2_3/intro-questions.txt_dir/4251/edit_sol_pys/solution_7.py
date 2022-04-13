
def main():
    n, m = map(int, input().split())
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().split())))
    print(solve(n, m, matrix))

def solve(n, m, matrix):
    # First, find the maximum value in each column
    max_vals = [max(row[i] for row in matrix) for i in range(m)]
    # Now, the max k is the max difference between any two elements in max_vals
    max_diff = 0
    for i in range(m):
        for j in range(i + 1, m):
            max_diff = max(max_diff, abs(max_vals[i] - max_vals[j]))
    return max_diff

if __name__ == "__main__":
    main()
