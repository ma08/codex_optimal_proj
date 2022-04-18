
import sys

def main():
    n,k = map(int,sys.stdin.readline().split())
    ans = 0
    for i in range(1,k+1):
        if i <= n:
            ans += n - i + 1

    print(ans**3)
if __name__ == '__main__':
    main()
