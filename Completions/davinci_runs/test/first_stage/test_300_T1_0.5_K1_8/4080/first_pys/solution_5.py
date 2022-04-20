

import sys

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    segments = []
    for _ in range(m):
        segments.append(list(map(int, input().split())))
    segments.sort(key=lambda x: x[1] - x[0], reverse=True)
    r = max(a)
    l = min(a)
    for segment in segments:
        if a[segment[0] - 1] >= a[segment[1] - 1]:
            for i in range(segment[0] - 1, segment[1]):
                a[i] -= 1
            r = max(a)
            l = min(a)
    print(r - l)
    print(0)


if __name__ == '__main__':
    sys.exit(main())