import sys

def main():
    n = int(sys.stdin.readline().rstrip())
    d = []
    for i in range(n):
        d.append(list(map(int, sys.stdin.readline().rstrip().split())))
    for i in range(n - 2):
        if d[i][0] == d[i][1] and d[i+1][0] == d[i+1][1] and d[i+2][0] == d[i+2][1]:
            print('Yes')
            exit(0)
    print('No')
    exit(0)

if __name__ == "__main__":
    main()
