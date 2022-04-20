

import sys

def main():
    n = int(input())
    t_a = list(map(int, input().split()))
    h = list(map(int, input().split()))
    ans = 0
    diff = sys.maxsize
    for i in range(len(h)):
        if abs(t_a[0] - h[i] * 0.006 - t_a[1]) < diff:
            diff = abs(t_a[0] - h[i] * 0.006 - t_a[1])
            ans = i + 1
    print(ans)

if __name__ == '__main__':
    main()