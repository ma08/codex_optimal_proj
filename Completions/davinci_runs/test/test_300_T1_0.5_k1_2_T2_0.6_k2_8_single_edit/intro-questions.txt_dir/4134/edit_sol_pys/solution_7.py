
def solve(n, m, k, grid):
    max_area = 0
    for i in range(n):
        for j in range(m):
            for l in range(1, min(n - i, m - j) + 1):
                area = l * l
                if area < max_area:
                    continue
                num_trees = 0
                for k in range(i, i + l):
                    for h in range(j, j + l):
                        if grid[k][h] == 1:
                            num_trees += 1
                if num_trees >= k:
                    max_area = max(max_area, area)
    return max_area

def main():
    n, m, k = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    print(solve(n, m, k, grid))

if __name__ == '__main__':
    main()
