import sys

def main():
    m, n, c = raw_input().split()
    m, n = int(m), int(n)
    frame1 = [raw_input().rstrip() for _ in range(m)]
    raw_input()
    frame2 = [raw_input().rstrip() for _ in range(m)]

    frame3 = []
    for i in range(m):
        frame3.append("")
        for j in range(n):
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
