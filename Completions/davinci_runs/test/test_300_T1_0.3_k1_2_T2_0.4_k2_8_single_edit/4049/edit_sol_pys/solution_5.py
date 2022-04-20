

import sys

def main():
    n = int(input())
    ans = []
    for i in range(n):
        a = list(map(int, input().split()))
        ans.append(a)
    print(ans)

if __name__ == "__main__":
    main()
