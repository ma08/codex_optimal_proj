

import sys

def main():
    line = sys.stdin.readline().strip().split(" ")
    n, k, x = int(line[0]), int(line[1]), int(line[2])
    line = sys.stdin.readline().strip().split(" ")
    a = [int(x) for x in line]
    a.sort()
    a.reverse()
    if x < k:
        print(-1)
        return
    if n == x:
        print(sum(a))
        return
    ans = 0
    for i in range(x):
        ans += a[i]
    for i in range(k-1, n-x, k):
        ans += a[i]
    print(ans)

if __name__ == "__main__":
    main()