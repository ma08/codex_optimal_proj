
import sys

def main():
    n = int(sys.stdin.readline())
    h = list(map(int, sys.stdin.readline().split()))
    cnt = 0
    for i in range(n):
        if h[i] >= max(h[:i+1]):
            cnt += 1
    print(cnt)

if __name__ == "__main__":
    main()
