
def main():
    n, m = map(int, input().split())
    rows = [list(map(int, input().split())) for _ in range(n)]
    print(solve(n, m, rows))

def solve(n, m, rows):
    # First, find the minimum value in each column
    min_vals = [min(row[i] for row in rows) for i in range(m)]
    # Now, the max k is the max difference between any two elements in min_vals
    max_k = 0
    for i in range(m - 1):
        max_k = max(max_k, abs(min_vals[i] - min_vals[i + 1]))
    return max_k

if __name__ == "__main__":
    main()
