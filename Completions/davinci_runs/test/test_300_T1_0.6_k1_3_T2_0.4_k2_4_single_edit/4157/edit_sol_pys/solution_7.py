
import math

def main():
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                print(max(abs(i - n // 2), abs(j - m // 2)))
                return

if __name__ == '__main__':
    main()
