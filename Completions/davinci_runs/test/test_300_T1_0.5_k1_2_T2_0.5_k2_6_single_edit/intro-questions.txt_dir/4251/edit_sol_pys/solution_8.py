
def main():
    n, m = map(int, input().split())
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().split())))
    print(solve(n, m, matrix))

def solve(n, m, matrix):
    min_vals = [min(row[i] for row in matrix) for i in range(m)]
    max_k = 0
    for i in range(m - 1):
        max_k = max(max_k, abs(min_vals[i] - min_vals[i + 1]))
    return max_k

if __name__ == "__main__":
    main()
