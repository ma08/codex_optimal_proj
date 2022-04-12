import sys

def main():
    N, M = [int(x) for x in sys.stdin.readline().strip().split()]
    grid = []
    for _ in range(N):
        grid.append(sys.stdin.readline().strip())
    for row in grid:
        print(row)

main()
