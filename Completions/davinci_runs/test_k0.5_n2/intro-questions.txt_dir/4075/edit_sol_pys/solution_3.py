
import sys

def main():
    n, m = map(int, sys.stdin.readline().strip().split())
    switches = [[] for _ in range(n)]
    for i in range(m):
        data = sys.stdin.readline().strip().split(' ')
        for j in range(1, len(data)):
            switches[int(data[j]) - 1].append(i)
    p = list(map(int, sys.stdin.readline().strip().split(' ')))
    ans = 0
    for i in range(2**n):
        light = True
        for j in range(n):
            if (i >> j) & 1:
                for k in switches[j]:
                    p[k] ^= 1
        for j in range(m):
            if p[j] == 1:
                light = False
        if light:
            ans += 1
        for j in range(n):
            if (i >> j) & 1:
                for k in switches[j]:
                    p[k] ^= 1
    print(ans)

if __name__ == '__main__':
    main()
