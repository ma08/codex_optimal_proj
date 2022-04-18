import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    arr = [list(sys.stdin.readline().strip()) for i in range(n)]
    for i in range(n):
        for j in range(m):
            if arr[i][j] == '_':
                print('YES')
                return
    print('NO')

main()
