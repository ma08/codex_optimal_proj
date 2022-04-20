

import sys

def main():
    n = int(input())
    ans = 0
    for i in range(1, n+1):
        if i == 1:
            ans = 2
        else:
            ans = (ans * 10) % 1000000007
    print(ans)

if __name__ == '__main__':
    main()