
def solve(n, m, k, grid):
    return ""

def main():
    n, m, k = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    ans = solve(n, m, k, grid)
    if ans == "":
        print("IMPOSSIBLE")
    else:
        print("POSSIBLE")
        print(ans)

if __name__ == '__main__':
    main()
