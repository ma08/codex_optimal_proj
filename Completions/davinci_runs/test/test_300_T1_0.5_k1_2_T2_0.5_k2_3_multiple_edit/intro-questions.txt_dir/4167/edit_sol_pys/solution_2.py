
import sys

def main():
    n,k = map(int,sys.stdin.readline().split())
    ans = 0
    for i in range(1,k+1):  # i = 1, 2, ... , k-1, k
            # i + 1, i + 2, ... , n
        ans += min(n-i+1,k-i+1)

    print(ans**3)

if __name__ == '__main__':
    main()
