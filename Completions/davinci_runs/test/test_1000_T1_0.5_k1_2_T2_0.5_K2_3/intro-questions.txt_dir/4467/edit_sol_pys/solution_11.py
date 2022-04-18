

import sys
input = sys.stdin.readline

def main():
    n = int(input())

    red = []
    blue = []

    for i in range(n):
        x, y = map(int, input().split())
        red.append((x, y))

    for i in range(n):
        x, y = map(int, input().split())
        blue.append((x, y))

    # red.sort(key=lambda x: x[0])
    red.sort(key=lambda x: x[1])
    blue.sort(key=lambda x: x[0])
    blue.sort(key=lambda x: x[1])

    count = 0
    for r in red:
        for b in blue:
            if r[0] < b[0] and r[1] < b[1]:
                count += 1
                blue.remove(b)
                break

    print(count)

if __name__ == "__main__":
    main()
