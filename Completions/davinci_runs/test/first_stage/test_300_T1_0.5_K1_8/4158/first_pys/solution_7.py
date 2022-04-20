

import sys

def main():
    n = int(input())
    x = list(map(int, input().split()))

    if n == 1:
        print(1)
        print(x[0])
        return
    if n == 2:
        if x[0] == x[1]:
            print(1)
            print(x[0])
            return
        else:
            print(2)
            print(x[0], x[1])
            return

    x.sort()

    x_dict = {}
    for i in x:
        if i not in x_dict:
            x_dict[i] = 1
        else:
            x_dict[i] += 1

    max_len = 0
    max_subset = []

    for i in range(len(x)):
        for j in range(i + 1, len(x)):
            diff = x[j] - x[i]
            if diff == 0:
                continue
            if diff % 2 == 1:
                continue
            diff = diff // 2
            if x[i] + diff not in x_dict:
                continue
            if x[j] + diff not in x_dict:
                continue
            if x[i] - diff not in x_dict:
                continue
            if x[j] - diff not in x_dict:
                continue
            subset = [x[i], x[j], x[i] + diff, x[j] + diff, x[i] - diff, x[j] - diff]
            subset.sort()
            if len(subset) > max_len:
                max_len = len(subset)
                max_subset = subset

    print(max_len)
    print(*max_subset)

if __name__ == '__main__':
    main()