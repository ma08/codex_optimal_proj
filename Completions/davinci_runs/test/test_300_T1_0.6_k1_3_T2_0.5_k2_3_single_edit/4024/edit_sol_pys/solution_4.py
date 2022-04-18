from collections import deque


def solve(n, a):
    a = deque(a)
    res = 0
    while a:
        f = a.popleft()
        if not a:
            res += f
            break
        s = a.pop()
        res += s
        if f > s:
            a.appendleft(f)
    return res


def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    print(solve(n, a))


if __name__ == "__main__":
    main()
