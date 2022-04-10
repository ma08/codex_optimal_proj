

import sys

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        curr = 1
        for j in range(i+1, n):
            if a[j] > a[j-1]:
                curr += 1
            else:
                break
        ans = max(ans, curr)
    print(ans)

if __name__ == "__main__":
    main()