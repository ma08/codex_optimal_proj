
import sys

def main():
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            ans = max(ans, (a[i][0] - a[j][0]) ** 2 + (a[i][1] - a[j][1]) ** 2)
    print(ans ** 0.5)

if __name__ == '__main__':
    main()
