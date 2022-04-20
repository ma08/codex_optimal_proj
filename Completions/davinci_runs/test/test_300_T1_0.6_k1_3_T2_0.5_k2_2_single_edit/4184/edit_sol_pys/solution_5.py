
import math
import sys


def main():
    n = int(input())
    w = list(map(int, input().split()))

    s_1 = []
    s_2 = []
    for i in range(n):
        s_1.append(sum(w[:i+1]))
        s_2.append(sum(w[i+1:]))
    ans = math.inf
    for i in range(n):
        ans = min(ans, abs(s_1[i] - s_2[i]))

    print(ans)


if __name__ == '__main__':
    main()
