

import sys

def main():
    n, m, c = input().split()
    n, m = int(n), int(m) # n = height, m = width
    frame1 = [input().rstrip() for _ in range(n)]
    input()
    frame2 = [input().rstrip() for _ in range(n)]

    frame3 = []
    for i in range(n):
        frame3.append("")
        for j in range(m):
            if frame1[i][j] == frame2[i][j]:
                frame3[i] += frame2[i][j]
            elif frame1[i][j] == c:
                frame3[i] += frame1[i][j]
            else:
                frame3[i] += frame2[i][j]

    for line in frame3:
        print(line)
    print()

if __name__ == '__main__':
    main()
