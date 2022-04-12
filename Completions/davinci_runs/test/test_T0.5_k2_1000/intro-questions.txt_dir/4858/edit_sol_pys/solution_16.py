
import sys

def main():
    M, N, C = sys.stdin.readline().rstrip().split()
    M, N = int(M), int(N) 
    frame1 = [sys.stdin.readline().rstrip() for _ in range(M)]
    sys.stdin.readline()
    frame2 = [sys.stdin.readline().rstrip() for _ in range(M)]

    frame3 = []
    for i in range(M):
        frame3.append("")
        for j in range(N):
            if frame1[i][j] == frame2[i][j]:
                frame3[i] += frame2[i][j]
            elif frame1[i][j] == C:
                frame3[i] += frame1[i][j]
            else:
                frame3[i] += frame2[i][j]

    for line in frame3:
        sys.stdout.write(line + '\n')
    sys.stdout.write('\n')

if __name__ == '__main__':
    main()
