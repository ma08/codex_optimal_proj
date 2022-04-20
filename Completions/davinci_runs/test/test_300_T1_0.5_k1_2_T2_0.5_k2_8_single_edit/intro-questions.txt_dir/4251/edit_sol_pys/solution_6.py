
def main():
    n, m = map(int, input().split())
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().split())))
    print(solve(n, m, matrix))

def solve(n, m, matrix):
    # First, find the minimum value in each row
    min_vals = [min(row) for row in matrix]
    # Now, the max k is the max difference between any two elements in min_vals,
    # so we just sort min_vals and take the last difference
    min_vals.sort()
    return min_vals[-1] - min_vals[0]

if __name__ == "__main__":
    main()
