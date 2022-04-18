
import sys

def main():
    h, w, n = [int(x) for x in sys.stdin.readline().split()]
    a = [int(x) for x in sys.stdin.readline().split()]
    a.sort()
    a.reverse()
    ans = [[0]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if i%2 == 0:
                ans[i][j] = a.pop()
            else:
                ans[i][w-j-1] = a.pop()
    for i in range(h):
        for j in range(w):
            print(ans[i][j], end=' ')
        print()

if __name__ == '__main__':
    main()
