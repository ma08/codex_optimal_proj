import sys

def test_case():
    n, m = map(int, sys.stdin.readline().split())
    c = []
    s = []
    for i in range(n):
        c.append(sys.stdin.readline()[:-1])
    for i in range(n):
        s.append(sys.stdin.readline()[:-1])
    num_robots = 0
    num_black_cells = 0
    for i in range(n):
        for j in range(m):
            if s[i][j] == 'U':
                if i > 0 and s[i-1][j] != 'D':
                    num_robots += 1
                    num_black_cells += c[i][j] == '0'
            elif s[i][j] == 'R':
                if j < m-1 and s[i][j+1] != 'L':
                    num_robots += 1
                    num_black_cells += c[i][j] == '0'
            elif s[i][j] == 'D':
                if i < n-1 and s[i+1][j] != 'U':
                    num_robots += 1
                    num_black_cells += c[i][j] == '0'
            elif s[i][j] == 'L':
                if j > 0 and s[i][j-1] != 'R':
                    num_robots += 1
                    num_black_cells += c[i][j] == '0'
    print(num_robots, num_black_cells)

t = int(sys.stdin.readline())
for i in range(t):
    test_case()