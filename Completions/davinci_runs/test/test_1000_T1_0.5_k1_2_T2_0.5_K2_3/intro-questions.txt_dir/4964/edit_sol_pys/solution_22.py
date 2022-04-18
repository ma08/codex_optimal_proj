

import sys

def main():
    N = int(sys.stdin.readline())  # N is number of movies
    movies = [int(sys.stdin.readline()) for _ in range(N)]
    max_profit = 0
    for i in range(1, N):
        max_profit = max(max_profit, max(movies[i:]) - min(movies[:i]))
    print(max_profit)

if __name__ == '__main__':
    main()
