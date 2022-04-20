

import sys
readline = sys.stdin.readline

def main():
    n = int(readline())
    l = list(map(int, readline().rstrip().split()))
    l.sort()
    ans = 0
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if l[i] + l[j] > l[k]:
                    ans += 1
    print(ans)

if __name__ == '__main__':
    main()