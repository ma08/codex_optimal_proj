from collections import deque


def solve(x, y, x1, y1, x2, y2):
    return min(min(y - y1, y2 - y), min(x - x1, x2 - x))


def main():
    q = deque()
    for _ in range(int(input())):
        x, y, x1, y1, x2, y2 = map(int, input().split())
        q.append(solve(x, y, x1, y1, x2, y2))
    for i in q:
        print(i)


if __name__ == "__main__":
    main()
