

import sys

def main():
    T = int(sys.stdin.readline())
    for _ in range(T):
        N = int(sys.stdin.readline())
        weights = [int(x) for x in sys.stdin.readline().split()]
        weights.sort()
        i = 0
        j = N - 1
        ans = 0
        while i < j:
            if weights[i] + weights[j] == weights[i] * 2:
                ans += 1
                i += 1
                j -= 1
            elif weights[i] + weights[j] > weights[i] * 2:
                j -= 1
            else:
                i += 1
        print(ans)


if __name__ == '__main__':
    main()
