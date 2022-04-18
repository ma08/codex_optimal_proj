#!/usr/bin/env python3
import sys

def main():
    rows, cols, c = sys.stdin.readline().split()
    rows, cols = int(rows), int(cols)
    frame1 = [sys.stdin.readline().rstrip() for _ in range(rows)]
    sys.stdin.readline()
    frame2 = [sys.stdin.readline().rstrip() for _ in range(rows)]

    frame3 = []
    for i in range(rows):
        frame3.append("")
        for j in range(cols):
            if frame1[i][j] == frame2[i][j]:
                frame3[i] += frame2[i][j]
            elif frame1[i][j] == c:
                frame3[i] += frame1[i][j]
            else:
                frame3[i] += frame2[i][j]

    for line in frame3:
        sys.stdout.write(line + '\n')
    sys.stdout.write('\n')

if __name__ == '__main__':
    main()
