
import sys


def main():
    N, M = sys.stdin.readline().split()
    N = int(N)
    M = int(M)
    grid = []
    for i in range(N):
        line = sys.stdin.readline().strip()
        grid.append(line)

    smallest_word = 'z'
    for n in range(N):
        for m in range(M):
            if grid[n][m] != '#':
                if n + 1 < N:
                    if grid[n + 1][m] != '#':
                        word = grid[n][m] + grid[n + 1][m]
                        if word < smallest_word: smallest_word = word
                if m + 1 < M:
                    if grid[n][m + 1] != '#':
                        word = grid[n][m] + grid[n][m + 1]
                        if word < smallest_word: smallest_word = word

    print(smallest_word)


if __name__ == '__main__':
    main()
