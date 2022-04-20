

import sys

def main():
    n = int(input())
    ans = 0
    for i in range(1, n+1):
        ans += i * (n-i+1)
    print(ans % (10**9+7))

if __name__ == "__main__":
    main()
