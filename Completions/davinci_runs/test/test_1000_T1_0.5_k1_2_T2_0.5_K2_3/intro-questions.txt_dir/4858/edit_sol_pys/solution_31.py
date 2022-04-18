

import sys

def main():
    for line in sys.stdin:
        m, n, c = map(int, line.split())
        
        frame_1 = []
        for i in range(m):
            frame_1.append(sys.stdin.readline().strip())
        
        sys.stdin.readline()
        
        frame_2 = []
        for i in range(m):
            frame_2.append(sys.stdin.readline().strip())
        
        frame_3 = []
        for i in range(m):
            frame_3.append('')
            for j in range(n):
                if frame_1[i][j] == c:
                    frame_3[i] += c
                elif frame_2[i][j] == c:
                    frame_3[i] += c
                else:
                    frame_3[i] += '.'
        
        for i in range(m):
            print(frame_3[i])
        
        print()

if __name__ == '__main__':
    main()
