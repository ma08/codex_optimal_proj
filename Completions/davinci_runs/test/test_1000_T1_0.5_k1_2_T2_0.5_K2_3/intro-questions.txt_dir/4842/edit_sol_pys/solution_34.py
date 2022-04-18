import sys

def main():
    n = int(sys.stdin.readline())
    v = [int(x) for x in sys.stdin.readline().split()] # read values
    d = [[0 for i in range(n)] for j in range(n)] # create matrix
    for i in range(n):
        d[0][i] = v[i] # fill first line
    for i in range(1, n):
        for j in range(n - i):
            d[i][j] = d[i - 1][j + 1] - d[i - 1][j]
    v_n = d[0][n - 1]
    for i in range(n - 1, -1, -1):
        v_n += d[i][0]
    for i in range(1, n):
        if d[i][0] != 0:
            print(i, v_n)
            return

if __name__ == '__main__':
    main()
