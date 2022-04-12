

from collections import deque


def merge(x):
    x = deque(x)
    while True:
        if not x:
            break
        if x[0] == 0:
            x.popleft()
        else:
            break
    while True:
        if not x:
            break
        if x[-1] == 0:
            x.pop()
        else:
            break
    if not x:
        return x
    i = 0
    while i < len(x) - 1:
        if x[i] == x[i + 1]:
            x[i] = x[i] * 2
            x.pop(i + 1)
        i += 1
    return x


def move_left(x):
    y = []
    for i in x:
        y.append(merge(i))
    return y


def move_right(x):
    y = []
    for i in x:
        y.append(list(reversed(merge(reversed(i)))))
    return y


def move_up(x):
    y = []
    for i in range(4):  # noqa
        y.append(merge([x[j][i] for j in range(4)]))
    return y


def move_down(x):
    y = []
    for i in range(4):  # noqa
        y.append(list(reversed(merge(reversed([x[j][i] for j in range(4)])))))
    return y


def move(x, d):
    if d == 0:
        x = move_left(x)
    elif d == 1:
        x = move_up(x)
    elif d == 2:
        x = move_right(x)
    elif d == 3:
        x = move_down(x)
    return x


def main():
    x = []
    for _ in range(4):
        x.append(list(map(int, input().split())))
    d = int(input())
    x = move(x, d)
    for i in range(4):  # noqa
        for j in range(4):  # noqa
            print(x[i][j], end=' ')
        print()


if __name__ == '__main__':
    main()
