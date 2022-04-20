

import math

def main():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))

    ans = 0
    min_diff = math.inf
    for i in range(n):
        diff = abs(a - (t - h[i] * 0.006))
        if diff < min_diff:
            ans = i
            min_diff = diff

    print(ans + 1)

if __name__ == "__main__":
    main()