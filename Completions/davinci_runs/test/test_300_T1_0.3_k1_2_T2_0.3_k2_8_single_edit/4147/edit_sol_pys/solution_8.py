
import sys

def main():
    n = int(sys.stdin.readline())
    a = [int(sys.stdin.readline()) for _ in range(n)]
    a.sort()
    b = [int(sys.stdin.readline()) for _ in range(n)]
    b.sort()
    c = [int(sys.stdin.readline()) for _ in range(n)]
    c.sort()
    d = [int(sys.stdin.readline()) for _ in range(n)]
    d.sort()
    ans = 0
    for i in range(n): # a
        for j in range(n): # b
            for k in range(n): # c
                for l in range(n): # d
                    if a[i] < b[j] and c[k] < d[l]:
                        ans += 1
    print(ans) 

if __name__ == '__main__':
    main()
