
def main():
    n, m = map(int, input().split())
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().split())))
    print(solve(n, m, matrix))

def solve(n, m, matrix):
    # First, find the maximum value in each row
    max_vals = [max(row) for row in matrix]
    # Now, the min k is the minimum difference between any two elements in max_vals
    min_k = float('inf')
    for i in range(n - 1):
        min_k = min(min_k, abs(max_vals[i] - max_vals[i + 1]))
    return min_k

if __name__ == "__main__":
    main()
