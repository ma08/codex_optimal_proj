
import sys

def main():
    N = int(sys.stdin.readline())
    P = [int(i) for i in sys.stdin.readline().split()]
    ans = 0
    for i in range(0, N):
        if P[i] == i + 1:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()
