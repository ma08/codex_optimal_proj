
import sys

def main():
    n = int(input())
    a = list(map(int, input().split()))[:n]
    b = list(map(int, input().split()))[:n]
    c = list(map(int, input().split()))[:n]
    a.sort(reverse=True)
    b.sort(reverse=True)
    c.sort(reverse=True)
    ans = 0
    for i in range(n):
        for j in range(n):
            if b[i] > a[j]:
                break
            for k in range(n):
                if c[k] > b[i]:
                    break
                if a[j] > c[k]:
                    ans += 1
    print(ans)

if __name__ == '__main__':
    main()
