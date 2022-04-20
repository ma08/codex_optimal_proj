

import sys

def main():
    # Read input
    n, m, c = [int(x) for x in sys.stdin.readline().split()]
    b_list = [int(x) for x in sys.stdin.readline().split()]
    a_list = []
    for i in range(n):
        a_list.append([int(x) for x in sys.stdin.readline().split()])
    # Solve
    ans = 0
    for i in range(n):
        ai_dot_b = 0
        for j in range(m):
            ai_dot_b += a_list[i][j] * b_list[j]
        if ai_dot_b + c > 0:
            ans += 1
    # Print
    print(ans)

if __name__ == '__main__':
    main()