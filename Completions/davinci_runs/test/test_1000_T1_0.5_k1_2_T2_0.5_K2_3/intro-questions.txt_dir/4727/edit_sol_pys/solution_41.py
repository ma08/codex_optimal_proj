

from collections import deque


def merge(list_x):
    list_x = deque(list_x)
    while True:
        if not list_x:
            break
        if list_x[0] == 0:
            list_x.popleft()
        else:
            break
    while True:
        if not list_x:
            break
        if list_x[-1] == 0:
            list_x.pop()
        else:
            break
    if not list_x:
        return list_x
    i = 0
    while i < len(list_x) - 1:
        if list_x[i] == list_x[i + 1]:
            list_x[i] = list_x[i] * 2
            list_x.pop(i + 1)
        i += 1
    return list_x


def move_left(list_x):
    list_y = []
    for i in list_x:
        list_y.append(merge(i))
    return list_y


def move_right(list_x):
    list_y = []
    for i in list_x:
        list_y.append(list(reversed(merge(reversed(i)))))
    return list_y


def move_up(list_x):
    list_y = []
    for i in range(4):
        list_y.append(merge([list_x[j][i] for j in range(4)]))
    return list_y


def move_down(list_x):
    list_y = []
    for i in range(4):
        list_y.append(list(reversed(merge(reversed([list_x[j][i] for j in range(4)])))))
    return list_y


def move(list_x, d):
    if d == 0:
        list_x = move_left(list_x)
    elif d == 1:
        list_x = move_up(list_x)
    elif d == 2:
        list_x = move_right(list_x)
    elif d == 3:
        list_x = move_down(list_x)
    return list_x


def main():
    list_x = []
    for _ in range(4):
        list_x.append(list(map(int, input().split())))
    d = int(input())
    list_x = move(list_x, d)
    for i in range(4):
        for j in range(4):
            print(list_x[i][j], end=' ')
        print()


if __name__ == '__main__':
    main()
