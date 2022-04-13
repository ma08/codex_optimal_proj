
import sys

def main():
    for line in sys.stdin:
        try:
            m, n, c = line.split()
            m = int(m)
            n = int(n)

            frame1 = []
            for i in range(m):
                frame1.append(sys.stdin.readline().strip())

            sys.stdin.readline()

            frame2 = []
            for i in range(m):
                frame2.append(sys.stdin.readline().strip())

            frame3 = []
            for i in range(m):
                frame3.append('')
                for j in range(n):
                    if frame1[i][j] == c:
                        frame3[i] += c
                    elif frame2[i][j] == c:
                        frame3[i] += c
                    else:
                        frame3[i] += '.'

            for i in range(m):
                print(frame3[i])

            print()
        except:
            pass

if __name__ == '__main__':
    main()
